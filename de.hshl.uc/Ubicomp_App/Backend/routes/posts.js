// Post allgemein  - in "Postman" Beispiel: http://localhost:3000/api/user/register 

var express = require('express');
const { find } = require('../models/Post');
var router = express.Router();
const app = express();




const Post = require('../models/Post');
const User = require('../models/User');
const verify = require('./verifyToken');
/* Old One:
router.post('/register', async (req, res) => {

    const user = new User({
        name: req.body.name,
        email: req.body.email,
        password: req.body.password

    });

    try{
        const savedUser = await user.save();
        res.send(savedUser);
    }catch(err){
        res.status(400).send(err);
    } 

    console.log(req.body);
});

    try {
        const savedPosted = await post.save();
        res.json(savedPosted);

    }catch(err) {
        res.json({ message: err });
    }
*/



//Submit a Post
router.post('/', async (req, res) => {
    //Post Request - to Json .body
    const post = new Post({
        title : req.body.title,
        description: req.body.description
    })
    //Response - to Json post
    try{
        const savedPost = await post.save()
        res.json(savedPost);
    }catch(error){
        res.json({ message: error});
    }
    //Console Output - savedPost Request of Json .body
    console.log(req.body);
});   

/*

//Get back all the Post, with "verify" als Middleware - for Token
router.get('/', verify, async(req, res) => {
    //Response - to Json post

    res.send(req.user);
  //  User.findOne({_id: req.user})
 /*   try {
        const posts = await Post.find();
        res.json({posts : {title:'my Token-Post', 
        description: 'random data you shouldnt access'}});
    } catch (error) {
        res.json({ message:error });
    }
    
});

*/



//Get back all the Post
router.get('/', async(req, res) => {
    //Response - to Json post
    try {
        const posts = await Post.find();
        res.json(posts);
    } catch (error) {
        res.json({ message:error });
    }
});




//Get back Specific Post per ID
router.get('/:postId', async (req, res) => {
    //Response - to Json post
    try {
        const post = await Post.findById(req.params.postId);
        res.json(post); 
    } catch (error) {
        res.json({ message: error });
    }  
});


//Delete Specific Post per ID
router.delete('/:postId', async (req, res) => {
    //Response - to Json removedPost
    try {
        const removedPost = await Post.deleteOne({ _id: req.params.postId })
        res.json(removedPost);
    } catch (error) {
        res.json( { message: error });
    }

});

//Update a Post per ID
router.patch('/:postId', async (req, res) => {
    //Response - to Json updatePost
    try {
        const updatedPost = await Post.updateOne(
            { _id: req.params.postId },
             {$set: {title: req.body.title}}
        );
        res.json(updatedPost);
    } catch (error) {
        res.json( { message: error });
    }

});


/*

router.get('/', function(req, res, next) {
    
    res.send("This is posts.js......")
    console.log("This is posts.js......");
});
*/
//Export to router
module.exports = router;