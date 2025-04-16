<!-- 
Create the front-end for your application using VueJS that will display the upload 
form. When the submit button is clicked it should make an AJAX request to the 
API route (endpoint) you created in Exercise 2. 
Start by first creating a new VueJS component called 'MovieForm' in a file called 
'MovieForm.vue' in your src/components folder. This component should have a 
'<template>' block that has the HTML code for the form. You will have to 
manually create the form fields. 
On the <form> tag, you will use the VueJS directive 
@submit.prevent="saveMovie". This will ensure that when the submit button is 
clicked or if the user press the ENTER key on their keyboard that the function 
saveMovie (which we will define next) in the quotes will be called. The .prevent 
will ensure that the default action for the form will be prevented. This is similar to 
the preventDefault() function that you used in INFO2180. 
Within your <form></form> tags you will need to create your form label and input 
tags for each field. For example: 
<div class="form-group mb-3"> 
<label for="title" class="form-label">Movie Title</label> 
<input type="text" name="title" class="form-control" /> 
</div>  
-->

<template>
    <h1>Upload Movie</h1>

    <form @submit.prevent="saveMovie" id="movieForm">
        <label>Movie Title</label>
        <input type="text" v-model="movie.title" name="movie.title" required />
        <br />

        <label>Movie Description</label>
        <input type="text" v-model="movie.description" required />
        <br />

        <label>Movie Poster</label>
        <input type="file" @change="setPoster" required />
        <br />

        <button type="submit">Save Movie</button>    
    </form>
</template>

<script>
import { ref } from 'vue';

const props = defineProps(['movie'])
const emit = defineEmits(['movieUploaded']);

let movie = ref({
    title: '',
    description: '',
    poster: null
});

const saveMovie = () => {
    const form = document.querySelector('#movieForm');
    const formData = new FormData();
    formData.append('title', movie.value.title);
    formData.append('description', movie.value.description);
    if (movie.value.poster) {
        formData.append('poster', movie.value.poster);
    }

    fetch('/api/v1/movies', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRF-Token': document.querySelector('meta[name="csrf-token"]').getAttribute('content')
        }
    })
    .then((resp)=>resp.json())
    .then((data)=>{
        console.log(data);
        emit('movieUploaded', data);
        movie.value = {
            title: '',
            description: '',
            poster: null
        };
    })
    .catch((error)=>{
        console.error('Error:', error);
    });
}


</script>