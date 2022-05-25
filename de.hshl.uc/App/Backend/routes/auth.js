//authantification - in "Postman" Beispiel: http://localhost:3000/api/user/register 

const router = require('express').Router();
//const bcrypt = require('bcryptjs/dist/bcrypt');
const User = require('../models/User');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const { registerValidation, loginValidation } = require('../validation');




//-------------------------------------------Get & Post on http://localhost:3001/api/user/register

//User Post
router.post('/register', async (req, res) => {
    
//Validate the Data before build a user
    const {error} = registerValidation(req.body);
   if(error) return res.status(400).send(error.details[0].message);

   //Checking if the Email is already in the database
   const emailExist = await User.findOne({email: req.body.email});
   if(emailExist) return res.status(400).send('Email already exists'), 
   console.log('Email already exists');

   //Hash password
    const salt = await bcrypt.genSalt(10);
    const hashPassword = await bcrypt.hash(req.body.password, salt);

//Create a new User
    //User Request - to Json .body
    const user = new User({
        name: req.body.name,
        email: req.body.email,
        password: hashPassword
    })
    //Response - to Json savedUser
    try{
        const savedUser = await user.save();
        //res.json({user: user._id});
        
    }catch(error){
        res.status(400).json({ message: error });
    } 
    //Console Output - User Request of Json .body
    console.log(req.body);
  
});


//Get back all User Posts
router.get('/register', async(req, res) => {
    //Response - to Json savedUser
    try {
        const savedUser = await User.find();
        
        res.json(savedUser);
        //console.log("Get /api/user/login:",  savedUser);
    } catch (error) {
        res.json({ message:error });
    }
});




//-------------------------------------------Get & Post on http://localhost:3001/api/user/login

//Get back all User Posts
router.get('/login', async(req, res) => {
    //Response - to Json savedUser
    try {
        const savedUser = await User.find();

        res.json(savedUser);
        
    } catch (error) {
    //    console.log("-----------GET ERROR /login Saved User:",  error);
        res.json({ message:error });
    }
});



router.post('/login', async (req,res) =>{
    //Validate the Data of Login before build a user
    const {error} = loginValidation(req.body);
    if(error) return res.status(400).send(error.details[0].message);
        //Checking if the Email doesn't is already in the database
        const user = await User.findOne({email: req.body.email});
        if(!user) return res.status(400).send('Email is not found'), 
        console.log('Email is not found');
        //Password is correct
        const validPass = await bcrypt.compare(req.body.password, user.password);
        if(!validPass) return res.status(400).send('Invalid password');
        console.log('Invalid password');
        
        
        //Create and assign a token
        const token = jwt.sign({_id: user._id}, process.env.TOKEN_SECRET);
        res.header('auth-token', token).send(token) ;    
        
        console.log('Logged in!');
        console.log('USER TOKEN:', token );
        //res.send('Logged in!');
        
})


//Export to router
module.exports = router;