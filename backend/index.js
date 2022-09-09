
const bodyParser = require("body-parser")
const mysql = require('mysql')
const app = require('express')()
const bcrypt = require('bcrypt')
const cors = require('cors')
const db = mysql.createPool({
    connectionLimit:100,
    host:'db',
    user:'root',
    password:'1234',
    database: 'pynance',
    port:'3306'

})
 
app.use(cors())
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }))

// parse application/json


app.set("view engine","ejs")



// app.use(function (req, res) {
//   res.setHeader('Content-Type', 'text/plain')
//   res.write('you posted:\n')
//   res.end(JSON.stringify(req.body, null, 2))
// })

app.get('/',(req,res)=>{
    res.render("register")
})

app.post('/register',async (req,res)=>{
  
    const data = req.body
 
    const salt = bcrypt.genSaltSync(10);
    const hashpass = await bcrypt.hash(data.password,salt);
    db.getConnection(async (err,conn)=>{
        if(err)console.log(err)
        console.log('DB connected success thread:'+conn.threadId)
        const sql ="select * from users where user=?"
        const query = mysql.format(sql,[data.user])
        const insert = "insert into users(user,username,password,email,api_key,api_secret,token) values (?,?,?,?,?,?,?)"
        const i_query = mysql.format(insert,[data.user,data.username,hashpass,data.email,data.api_key,data.api_secret,data.token])

        await conn.query(query,async (err,result)=>{
            if(err)throw(err)
            if(result.length!=0){
                conn.release()
                console.log("----> User already exists <----")
                res.sendStatus(409)
            }else {
                await conn.query(i_query,(err,result)=>{
                    if(err)throw(err)
                    console.log(`-----> Register Complete ${result.insertId} <------`)
                    res.sendStatus(201)
                })
            }
        })
    })
     
})

app.post('/login',(req,res)=>{
    const data = req.body
    
    db.getConnection(async (err,conn)=>{
        if(err)throw(err)
        const sql = "select * from users where email=? or user=?"
        const query = mysql.format(sql,[data.email,data.email])
        await conn.query(query,async (err,result)=>{
            conn.release()
            if(err)throw(err)
            if(result.length == 0){
                console.log("-----> User not exists <-----")
                res.sendStatus(404)
            }else {
                const hashpass = result[0].password
                if(await bcrypt.compare(data.password,hashpass)){
                    console.log("-----> Login Success <-----")
                    res.json({username:result[0].user,msg:'logged in!'})
                }else {
                    console.log("-----> Password or User Incorrect! <-----")
                    res.send(`Invalid`)
                }
            }
        })
    })
    //res.status(200).json({'username':data.email,'msg':'Login success'})
})

app.listen('3000',()=>{
    console.log('Backend running on http://locahost:3000')
})