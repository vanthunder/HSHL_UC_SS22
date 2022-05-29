const mongoose = require('mongoose')

const UserSchema = new mongoose.Schema({
    user:String,
    message:String,
})

mongoose.model("Chatmessages",UserSchema)