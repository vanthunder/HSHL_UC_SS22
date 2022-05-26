const jwt = require('jsonwebtoken');

//Middleware function - can be added to any route to protect/private it
module.exports = function auth (req, res, next){
    const token = req.header('auth-token');
    if(!token) return res.status(401).send('Access Denied');

    try {
        const verified = jwt.verify(token, process.env.TOKEN_SECRET);
        req.user = verified;
        next();
    } catch (error) {
        res.status(400).send('Invalid Token');
    }
}