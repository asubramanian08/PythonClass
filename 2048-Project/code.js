const http = require('http');
var fs = require('fs');

const hostname = '127.0.0.1';
const port = 3000;

fs.readFile('index.html', function (err, html) {
    if (err) throw err;
    http.createServer(function (request, response) {
        response.writeHeader(200, { "Content-Type": "text/html" });
        response.write(html);
        response.end();
    }).listen(port);
});

// terminal: node code.js

// const server = http.createServer((req, res) => {
//     res.statusCode = 200;
//     res.setHeader('Content-Type', 'text/plain');
//     res.end('Hello World');
// });

// server.listen(port, hostname, () => {
//     console.log(`Server running at http://${hostname}:${port}/`);
// });

// server link: http://127.0.0.1:3000