const http = require('http')
const hello = require('./my_module')

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
	res.statusCode = 200;
	res.write(hello.hello_world());
	res.end();
	});

server.listen(port, hostname, () => {
	console.log('Server is running at http://127.0.0.1:3000');
	});
    
