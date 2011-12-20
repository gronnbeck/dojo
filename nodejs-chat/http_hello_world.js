var http = require('http');

var server = http.createServer(function(req, res){
	res.writeHeader(200);
	res.write("Hello World!");
	res.end();
});

server.listen(8000);
