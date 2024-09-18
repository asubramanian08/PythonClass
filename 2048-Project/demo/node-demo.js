var http = require('http');
var url = require('url');
var add = require('./module-demo.js');

http.createServer(function (req, res) {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.write('Hello World!');
    var q = url.parse(req.url, true).query;
    res.end(add.add(q.a, q.b).toString()); // http://localhost:8080/?a=4&b=4
}).listen(8080);