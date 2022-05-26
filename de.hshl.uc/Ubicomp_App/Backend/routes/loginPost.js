/*

// Post allgemein  - in "Postman" Beispiel: http://localhost:3000/api/user/register 

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





/*

router.get('/', function(req, res, next) {
    
    res.send("This is posts.js......")
    console.log("This is posts.js......");
});

//Export to router
module.exports = router;

*/