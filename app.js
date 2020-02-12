const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.text({ type: "text/plain" }));
app.use(bodyParser.json());
app.use(cors({
  // origin: 'http://127.0.0.1:5500/public/index.html'
}));

const port = 8080;
app.use(express.static('public'))
app.listen(port, function () {
  console.log("server listening on port ", port);
});

app.get('/api/*', (req, res)=>{
  //request variable
  const __query = req.query || null,
    __path = req.path,
    __protocol = req.protocol,
    __method = req.method,
    __secure = req.secure,
    __headers = req.headers;
  //send response
  return res
    .status(200)
    .json({
      "status": "Ok",
      "path": __path,
      "protocol": __protocol,
      "method": __method,
      "secure": __secure,
      "headers": __headers,
      "query": __query,
    });
});

app.post('/api/*', (req, res)=>{
  const __query = req.query || null,
    __body = req.body || null,
    __path = req.path,
    __protocol = req.protocol,
    __method = req.method,
    __secure = req.secure,
    __headers = req.headers;
  //send response
  return res
    .status(200)
    .json({
      "status": "Ok",
      "path": __path,
      "protocol": __protocol,
      "method": __method,
      "secure": __secure,
      "headers": __headers,
      "query": __query,
      "body": __body
    });
});

app.put('/api/*', (req, res)=>{
  const __query = req.query || null,
    __body = req.body || null,
    __path = req.path,
    __protocol = req.protocol,
    __method = req.method,
    __secure = req.secure,
    __headers = req.headers;
  //send response
  return res
    .status(200)
    .json({
      "status": "Ok",
      "path": __path,
      "protocol": __protocol,
      "method": __method,
      "secure": __secure,
      "headers": __headers,
      "query": __query,
      "body": __body
    });
});

app.delete('/api/*', (req, res)=>{
  const __query = req.query || null,
    __body = req.body || null,
    __path = req.path,
    __protocol = req.protocol,
    __method = req.method,
    __secure = req.secure,
    __headers = req.headers;
  //send response
  return res
    .status(200)
    .json({
      "status": "Ok",
      "path": __path,
      "protocol": __protocol,
      "method": __method,
      "secure": __secure,
      "headers": __headers,
      "query": __query,
      "body": __body
    });
});