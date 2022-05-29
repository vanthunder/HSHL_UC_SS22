var createError = require('http-errors');
var express = require('express');
var app = express();
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
//----------------------selbst eingefügt
var cors = require('cors');
//-------------------------------
var indexRouter = require('./routes');
var usersRouter = require('./routes/users');
//----------------------selbst eingefügt
testAPIRouter = require('./routes/testAPI');
testAPIRouter2 = require('./routes/testAPIP');
const bodyParser = require('body-parser'); //-----------------------------------------------------------neu













//Middlewares
app.use(cors());
app.use(bodyParser.json());                     //-----------------------------------------------------------neu







//---------------------Start Server

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(express.json());
//----------------------selbst eingefügt
//cross-origin resource sharing - allow the react App 
//to communicate from another hosted domain to this particular domain server
app.use(cors());
//-------------------------------
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/users', usersRouter);





//-----------------------------------------------------------neu

//Use the Middleweare of routes/testAPI.js with URL "/api/testAPI"
app.use('/testAPI', testAPIRouter);
//Use the Middleweare of routes/testAPI.js with URL "/api/testAPIP"
app.use('/testAPIP', testAPIRouter2);



//Import Routes

// Posts in Folder routes/posts.js 
const postsRoute = require('./routes/posts');
//Register und Login Route in Folder routes/auth.js
const authRoute = require('./routes/auth');


//Route Middlewares

//Use the Middleweare of routes/posts.js with URL "/api/posts"
app.use('/api/posts', postsRoute);
//Use the Middleweare of routes/auth.js with URL "/api/user/register" & "/api/user/login"
app.use('/api/user/', authRoute);



//-----------------------------------------------------------neu




// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});


console.log('Sever starts...');







//---------------------connect to MongoDB

 


const dotenv = require('dotenv');
const mongoose = require('mongoose');
//const bodyParser = require('body-parser');
dotenv.config();



//Middlewares
//app.use(cors());
//app.use(bodyParser.json());                     //-----------------------------------------------------------neu
//app.use(express.json());
/*
//Import Routes
const postsRoute = require('./routes/posts');
const authRoute = require('./routes/auth');
//const bodyParser = require('body-parser');

//Route Middlewares
app.use('/api/user', authRoute);
app.use('/api/posts', postsRoute);
*/
//Routes
app.get('/', (req, res) => {
    res.send('We are on home');
});




//Connect to DB
mongoose.connect(process.env.DB_CONNECT, { useNewUrlParser: true,  useUnifiedTopology: true },
    () => console.log('connected to DB!')
);





module.exports = app;