// Post allgemein  - in "Postman" Beispiel: http://localhost:3000/api/user/register 

const mongoose = require('mongoose');
/*
// User Shema
const userSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
        min: 6,
        max: 255 
    },
    email: {
        type: String,
        required: true,
        max: 255,
        min: 6
    },
    password: {
        type: String,
        required: true,
        max: 1024,
        min: 6
    },
    date: {
        type: Date,
        default: Date.now
    }
    
});
*/

//Post Shema
const postSchema = mongoose.Schema({
    //Title Specs
    title: {
        type: String,
        required: true
    },
    //Description Specs
    description: {
        type: String,
        required: true
    },
    //Date Specs
    date: {
        type: Date,
        default: Date.now
    }
},
    //Collection address on mongoDB
    {collection : 'posts'});



//Export to mongoose/mongoDB
module.exports = mongoose.model('Post', postSchema);
