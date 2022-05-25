/*

const express = require ('express');
const app = express();
const dotenv = require('dotenv');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');
//require('dotenv/config');
require('dotenv').config();
//Import Routes
//const authRoute = require('./routes/authentification');



//Middlewares
app.use(cors());
app.use(bodyParser.json());

//Import Routes
const postsRoute = require('./routes/posts');
const authRoute = require('./routes/auth');

//Route Middlewares
app.use('/api/user', authRoute);
app.use('/api/posts', postsRoute);

//Routes
app.get('/', (req, res) => {
    res.send('We are on home');
});

//dotenv.config();

//Connect to DB
mongoose.connect(process.env.DB_CONNECT, { useNewUrlParser: true,  useUnifiedTopology: true },
    () => console.log('connected to DB!')
);





//Middleware
//app.use(express.json({ type: 'application/*+json' }));
//Route Middlewares
//app.use('/api/user', authRoute);

//----------------------------------------------------------------------------von 3000 auf 5000 geändert!!!!!!!!!!!!!!!!!!!!!!!!!!!

app.listen(5000, () => console.log('Server up and running'));

*/