const http = require('http');
var fs = require('fs');

const hostname = '127.0.0.1';
const port = 3000;

http.createServer(function (request, response) {

    response.writeHeader(200);
    let filename = "." + request.url;
    if (request.url === "/") {
        filename = "./index.html";
    }
    let fileContents = fs.readFileSync(filename);
    response.write(fileContents);
    response.end();
}).listen(port);

// terminal: node code.js
// server link: http://127.0.0.1:3000