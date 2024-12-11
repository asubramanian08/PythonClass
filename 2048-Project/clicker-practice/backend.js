const http = require('http');
var fs = require('fs');

const hostname = '127.0.0.1';
const port = 3000;

http.createServer(function (request, response) {

    count = 0;

    if (request.url == "/increment" && request.method == "POST") {
        // Increment the counter
   
            count ++;
            response.write(count);
         
    }
    else if (request.method == "GET") {
        // Load the file
    
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