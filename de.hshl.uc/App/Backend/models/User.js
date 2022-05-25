// User  - in "Postman" Beispiel: http://localhost:3000/api/user/register 

const mongoose = require('mongoose');
//User Shema
const userSchema = mongoose.Schema({
    //Name Specs
    name: {
        type: String,
        required: true,
        min: 6,
        max: 255 
    },
    //Email Specs
    email: {
        type: String,
        required: true,
        max: 255,
        min: 6
    },
    //Password Specs
    password: {
        type: String,
        required: true,
        max: 1024,
        min: 6
    },
    //Date Specs
    date: {
        type: Date,
        default: Date.now
    }
},
    //Collection address on MongoDB
    {collection : 'users'});



//Export to mongoose/mongoDB
module.exports = mongoose.model('User', userSchema);
