const express = require('express')
const app = express ()
const bodyParser = require('body-parser')
const mongoose = require('mongoose')
require('./User')

app.use(bodyParser.json())

const User = mongoose.model('user')


const mongoUri = "mongodb+srv://Damon:UbiComp@awd-cluster1.kbtax.mongodb.net/?retryWrites=true&w=majority"

mongoose.connect(mongoUri,{
    useNewUrlParser:true,
    useUnifiedTopology:true
})

mongoose.connection.on("connected",()=>{
    console.log("connected to MongoDB")
})
mongoose.connection.on("error",(err)=>{
    console.log("error",err)
})

app.get('/',(req,res)=>{
    User.find({}).then(data=>{
        res.send(data)
    }).catch(err=>{
        console.log(err)
    })
})


app.post('/send-data',(req,res)=>{
    const user = new User({
        name:req.body.name,
        password:req.body.password
    })
    user.save()
    .then(data=>{
        console.log(data)
        res.send(data)
    }).catch(err=>{
        console.log(err)
    })
    
})

app.post('/delete',(req,res)=>{
    User.findByIdAndRemove(req.body.id)
    .then(data=>{
        console.log(data)
        res.send("deleted")
    }).catch(err=>{
        console.log(err)
    })
    
})

app.post('/update',(req,res)=>{
    User.findByIdAndUpdate(req.body.id,{
        name:req.body.name,
        password:req.body.password
    }).then(data=>{
        console.log(data)
        res.send(data)
    })
    .catch(err=>{
        console.log(err)
    })
})

app.listen(3000,()=>{
    console.log('server running')
})

