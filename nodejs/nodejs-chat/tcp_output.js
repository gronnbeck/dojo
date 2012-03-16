var net = require('net')

var server = net.createServer(function(socket){
	socket.write("Hello World\n");
	socket.on('data', function(data){
		socket.write("You wrote: " + data);
	})
});

server.listen(8000);