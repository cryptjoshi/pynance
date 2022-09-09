import sequelize from '../sequelize';
import User from './User'
import UserLogin from  './UserLogin'
function sync(...args){
    return sequelize.sync(...args)
}

User.hasMany(UserLogin, {
    foreignKey: 'userId',
    as: 'logins',
    onUpdate: 'cascade',
    onDelete: 'cascade',
  });

export default { sync}
export {
    User,
    UserLogin
}