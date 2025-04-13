from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config
from app.models import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app,db)

from app import views

app.config['UPLOAD_FOLDER'] = 'uploads'

if __name__ == '__main__':
    app.run(debug=True)

# Import views AFTER app is created to avoid circular import

###
# from flask import Flask
# from flask_migrate import Migrate
# from app.config import Config
# from app.models import db  # import db from models

# app = Flask(__name__)
# app.config.from_object(Config)

# db.init_app(app)
# migrate = Migrate(app, db)

# from app import views  # import after db & app are set up

# if __name__ == '__main__':
#     app.run(debug=True)