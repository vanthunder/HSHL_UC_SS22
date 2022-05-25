var express = require('express');
var router = express.Router();
const app = express();





const Post = require('../models/Post');
const User = require('../models/User');
const verify = require('./verifyToken');




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

/*
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
*/


router.get('/', function(req, res, next) {
    res.send("This is testAPI......")
    console.log("This is testAPI......");
});




module.exports = router;

