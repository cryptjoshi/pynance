import DataType from 'sequelize';
import Model from '../sequelize';
import bcrypt from 'bcrypt';
import { NULL } from 'graphql/language/kinds';
const User = Model.define('User', {
    userId: {
        type: DataType.UUID,
        defaultValue: DataType.UUIDV1,
        primayKey: true
    },
    user:{
        type:DataType.STRING,
        allowNull:false,
        defaultValue: false

    },
    username:{
        type:DataType.STRING,
        allowNull:false,
        defaultValue: false
    },
    email:{
        type:DataType.STRING,
        allowNull:false,
        defaultValue: false
    },
    password:{
        type:DataType.STRING,
        allowNull:false

    },
    api_key:{
        type:DataType.STRING,
        allowNull:false,
        defaultValue: false

    },
    api_secret:{
        type:DataType.STRING,
        allowNull:false,
        defaultValue: false

    },
    token:{
        type:DataType.STRING,
        allowNull:false,
        defaultValue: false

    }
},{classMethods: {
    generateHash: function(password){
        return bcrypt.hashSync(password,bcrypt.genSalt(10),null)
    },
    indexs: [
        {fields: ['user','email']}
    ]
}})

export default User