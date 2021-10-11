const http = require('http')
const welcome = require('./welcome')

const hostname = '127.0.0.1';
const port = 8080;

const server = http.createServer((req,res) =>{
    res.statusCode = 200;
    res.write(welcome.welcome());
    res.end();
})

server.listen(port, hostname, () => {
    console.log('Server is running at http://127.0.0.1:8080');
})