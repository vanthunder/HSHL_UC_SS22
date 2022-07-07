const express = require('express')
const app = express()
const bodyParser = require('body-parser')
const mongoose = require('mongoose')
const cors = require('cors')
require('./Chat')

app.use(bodyParser.json())

app.use(function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "http://localhost:8080/");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});
app.options('http://localhost:8080/', cors())

const corsOptions = {
    origin: 'http://localhost:8080/',
    optionsSuccessStatus: 200,
    methods: "GET, PUT, POST, DELETE"
}


app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    next();
});

const Chat = mongoose.model('Chatmessages')


const mongoUri = "mongodb+srv://Damon:UbiComp@awd-cluster1.kbtax.mongodb.net/?retryWrites=true&w=majority"


mongoose.connect(mongoUri, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
    dbName: "Chat_Application"
})

mongoose.connection.on("connected", () => {
    console.log("connected to MongoDB")
})
mongoose.connection.on("error", (err) => {
    console.log("error", err)
})

app.get('/', (req, res) => {
    User.find({}).then(data => {
        res.send(data)
    }).catch(err => {
        console.log(err)
    })
})


app.post('/send-data', (req, res) => {
    const chat = new Chat({
        message: req.body.message
    })
    chat.save()
        .then(data => {
            console.log(data)
            res.send(data)
        }).catch(err => {
        console.log(err)
    })

})
/** Die folgenden Befehle sind dazu gedacht, Daten auf der MonoDB auf den neusten Stand
    zu bringen oder zu entfernen: 
 
app.post('/delete', (req, res) => {
    User.findByIdAndRemove(req.body.id)
        .then(data => {
            console.log(data)
            res.send("deleted")
        }).catch(err => {
        console.log(err)
    })

})

app.post('/update', (req, res) => {
    User.findByIdAndUpdate(req.body.id, {
        name: req.body.name,
        password: req.body.password
    }).then(data => {
        console.log(data)
        res.send(data)
    })
        .catch(err => {
            console.log(err)
        })
})
 */

app.use(express.json())
app.use(cors(corsOptions));
const port = process.env.PORT || 1666;
app.listen(port, () => {
    console.log('server running')
})