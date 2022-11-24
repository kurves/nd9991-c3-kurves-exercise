let express = require('express');
let app = express();

console.log("Hello World");
app.get("/", (req,res)=>{
    res.send("Hello Express");
});

app.get("/", (req,res)=>{
    res.sendFile(__dirname + "/public/index.html");
});

app.get("/json", (req,res) => {
    res.json({mesaage: "Hello Json"});
});


app.get('/now', (req,res)=>{
    req.time = new Date().toString();
    next();
}, (req,res)=>{
    res.json({time: "req.time"});
})





























 module.exports = app;
