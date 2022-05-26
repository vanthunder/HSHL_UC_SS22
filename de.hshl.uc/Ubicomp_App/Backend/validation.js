//Validation
const Joi = require('joi');
 //const validation = Joi.valid(req.body, schema);
 //  const {error} = schema.validate(req.body);

 
//Register Validation shema
const registerValidation = (data) => {

    const schema = Joi.object({
        name: Joi.string()
            .min(6)
            .required(),
        email: Joi.string()
            .min(6)
            .required()
            .email(),
        password: Joi.string()
            .min(6)
            .required()
    });
    return {error} = schema.validate(data);
}

//Login Validation shema
const loginValidation = (data) => {

    const schema = Joi.object({
        email: Joi.string()
            .min(6)
            .required()
            .email(),
        password: Joi.string()
            .min(6)
            .required()
    });
    return {error} = schema.validate(data);
}
module.exports.registerValidation = registerValidation;
module.exports.loginValidation = loginValidation;