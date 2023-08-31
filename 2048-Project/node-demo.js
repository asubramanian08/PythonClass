var http = require('http');
var url = require('url');

http.createServer(function (req, res) {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.write('Hello World!');
    res.end(url.parse(req.url, true).query.name);
}).listen(8080);

// http://localhost:8080/?var=<br>On-a-new-line