const mongoose = require('mongoose')

const UserSchema = new mongoose.Schema({
    message:String,
})

mongoose.model("Chatmessages",UserSchema)