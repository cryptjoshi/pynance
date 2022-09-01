
const bodyParser = require("body-parser")

const app = require('express')()


app.use(bodyParser.urlencoded({ extended: false }))

// parse application/json
app.use(bodyParser.json())

// app.use(function (req, res) {
//   res.setHeader('Content-Type', 'text/plain')
//   res.write('you posted:\n')
//   res.end(JSON.stringify(req.body, null, 2))
// })

app.get('/',(req,res)=>{
    res.send('Welcome to Backend')
})

app.post('/register',(req,res)=>{
    res.send('register')
})

app.post('/login',(req,res)=>{
    const data = req.body
    console.log(data)
    res.status(200).json({'username':data.email,'msg':'Login success'})
})

app.listen('3000',()=>{
    console.log('Backend running on http://locahost:3000')
})