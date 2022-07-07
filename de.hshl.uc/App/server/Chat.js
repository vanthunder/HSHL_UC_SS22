const mongoose = require('mongoose')

/**Erstellen eines Schemas wie die Daten auf der MongoDB abgespeichtert werden */
const UserSchema = new mongoose.Schema({
    message:String,
})

mongoose.model("Chatmessages",UserSchema)