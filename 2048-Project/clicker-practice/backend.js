const http = require('http');
var fs = require('fs');

const hostname = '127.0.0.1';
const port = 3000;

http.createServer(function (request, response) {

    if (request.url == "/increment" && request.method == "POST") {
        // ...
    }
    else if (request.method == "GET") {
        // ...
    
        response.writeHeader(200);
        let filename = "." + request.url;
        if (request.url === "/") {
            filename = "/frontend.html";
        }
        let fileContents = fs.readFileSync(filename);
        response.write(fileContents);
        response.end();
    }
}).listen(port);

x = 0;

if (){

};