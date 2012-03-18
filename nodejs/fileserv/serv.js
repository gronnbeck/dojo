var net = require('net');
var fs = require('fs');

var server = net.createServer(function (socket) {
	console.log('server connected');
	socket.on('data', function(data) {
		req = JSON.parse(data);
		if (req.cmd == 'checkout') {
			console.log('sending file to client');
			var checkout = net.createServer(function (socket) {
				console.log('checkout connected');
				fs.readFile(req.checkout.file, function(data) {
					socket.write(data);
					socket.pipe(socket);
				});
				socket.close()
			});
			checkout.listen(8887, function () {
				console.log("waiting on client to connect");
			});
		}
		if (req.cmd == 'push') {
			console.log('receiving file');
			var push = net.createServer(function (socket) {
				console.log('push connected');
				socket.on('data', function(data) {
					fs.writeFile(req.push.file, data);
				});
				socket.on('end', function() {
					console.log("Data received. Verify?");
				});
			});		
			push.listen(8889, function () {
				console.log("waiting for client to push file");
				socket.write("8889");
				socket.pipe(socket);
			});
		//	fs.writeFile(req.push.file, req.push.data);
		}
		console.log('ok got your data');
	});
	socket.on('end', function () {
		console.log('server disconnected');
	});
});

server.listen(8888, function() {
	console.log('server bound');
});
