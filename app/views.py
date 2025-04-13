"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, jsonify, send_file
from app.models import Movie
from app.forms import MovieForm
from werkzeug.utils import secure_filename
from psycopg2.extras import RealDictCursor
import psycopg2
from flask import jsonify
from flask import render_template, request, jsonify
import os


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


@app.route('/api/v1/movies', methods=['POST'])
def movies():
    form = MovieForm()

    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        poster = form.poster.data

        # Save the file
        filename = secure_filename(poster.filename)
        poster.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Save movie to database
        movie = Movie(title=title, description=description, poster=filename)
        db.session.add(movie)
        db.session.commit()

        return jsonify({
            "message": "Movie Successfully added",
            "title": title,
            "poster": filename,
            "description": description
        }), 201

    # If validation fails
    return jsonify({"errors": form_errors(form)}), 400

###
# The functions below should be applicable to all Flask apps.
###

# @app.route('/api/v1/movies', methods=['POST'])
# def movies():
#     form = MovieForm()

#     if form.validate_on_submit():
#         title = form.title.data
#         description = form.description.data
#         poster = form.poster.data

#         if poster:
#             filename = secure_filename(poster.filename)
#             poster.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

#         try:
#             data=request.json

#             required_fields = ['title', 'description', 'poster']
#             if not all(field in data for field in required_fields):
#                 return jsonify({"errors":[{},{}]}), 400

#             db = psycopg2.connect(**db_config)
#             cursor = db.cursor(cursor_factory=RealDictCursor)
#             cursor.execute("""
#                 INSERT INTO movies (title, description, poster) 
#                 VALUES (%s, %s, %s)
#             """, (
#                     data['title'], 
#                     data['description'], 
#                     filename
#                 ))
            
#             movies = cursor.fetchall()
            
#             db.commit()
#             cursor.close()
#             db.close()

#             return jsonify({
#                 "message": "Movie Successfully added",
#                 "title": data['title'],
#                 "poster": filename,
#                 "description": data['description']
#             }), 201
#         except Exception as e:
#             return jsonify({"errors":[{},{}]}), 500


# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404