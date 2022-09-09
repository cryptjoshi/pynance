import {
    GraphQLList as List,
    GraphQLString as StringType,
    GraphQLInt as IntType,
    GraphQLNonNull as NonNull

} from 'graphql'

import UserLoginType from '../types/userLoginType'

// Authentication Utils
import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';
import { auth } from '../../config';

import {User,UserLogin} from '../models'

const userLogin = {
    type: UserLoginType,
    args: {
        email: { type: new NonNull(StringType)},
        password:{type: new NonNull(StringType)}
        
    },
    async resolve({request,response},{
        email,password
    }) {
        if(!request.user){
            const userLogin = await User.findOne({
                attributes: ['id','email','password','userBanStatus','userDeleteAt'],
                where: {
                    email: email,
                    userDeleteAt: null
                }
            })
            if(userLogin){
                if(bcrypt.compareSync(password,userLogin.password)){
                    if(userLogin.userBanStatus ==1) {
                        return {
                            status: "userbanned"
                        }
                    }else if(userLogin.userDeleteAt !=null) {
                        return {
                            status: "userDeleted"
                        }
                    
                    } else {
                        const expireIn = 60 * 60 * 24 * 180 // 190 days
                        const token = jwt.sign({id:userLogin.id,email:userLogin.email},auth.jwt.secret,{expireIn})
                        response.cookie('id_token',token,{maxAge: 1000 * expireIn,httpOnly: true})
                        return {
                            status: "success"
                        }
                    }
                } else {
                    return {
                        status: "password"
                    }
                } 
            } else {
                return {
                    status: "email"
                }
            }
        } else {
            if(request.user.admin == true){
                return {
                    status: "adminLoggedIn"
                }
             } else {
                return {
                    status: "loggedIn"
                }
             }
        }
    }
}

export default userLogin