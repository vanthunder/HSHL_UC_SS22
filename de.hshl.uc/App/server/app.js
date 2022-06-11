const express = require('express')
const app = express()
const bodyParser = require('body-parser')
const mongoose = require('mongoose')
const cors = require('cors')
const Server = require("socket.io")
const socketio = require('socketio')
require('./User')
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

app.get('/jokes/random', (req, res) => {
    request(
        {url: 'https://joke-api-strict-cors.appspot.com/jokes/random'},
        (error, response, body) => {
            if (error || response.statusCode !== 200) {
                return res.status(500).json({type: 'error', message: err.message});
            }

            res.json(JSON.parse(body));
        }
    )
});


//const User = mongoose.model('user')
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

app.use(function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "YOUR-DOMAIN.TLD"); // update to match the domain you will make the request from
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

app.get('/', function (req, res, next) {

    app.post('/send-data', (req, res) => {
        const chat = new Chat({
            user: req.body.name,
            message: req.body.password
        })
        chat.save()
            .then(data => {
                console.log(data)
                res.send(data)
            }).catch(err => {
            console.log(err)
        })

    })
    // Handle the get for this route
});

app.post('/', function (req, res, next) {
    // Handle the post for this route

    app.post('/send-data', (req, res) => {
        const chat = new Chat({
            user: req.body.name,
            message: req.body.password
        })
        chat.save()
            .then(data => {
                console.log(data)
                res.send(data)
            }).catch(err => {
            console.log(err)
        })

    })
});


app.get('/', (req, res) => {
    User.find({}).then(data => {
        res.send(data)
    }).catch(err => {
        console.log(err)
    })
})


app.post('/send-data', (req, res) => {
    const chat = new Chat({
        user: req.body.name,
        message: req.body.password
    })
    chat.save()
        .then(data => {
            console.log(data)
            res.send(data)
        }).catch(err => {
        console.log(err)
    })

})

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
app.use(express.json())
app.use('/api/user', Chat)
app.use(cors(corsOptions));
//const io = socketio(Server).sockets;
const port = process.env.PORT || 1666;
//console.log(io.handshake.host);
app.listen(port, () => {
    console.log('server running')
})