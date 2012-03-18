var express = require('express');
var io 		= require('socket.io');

var app  = express.createServer()
	, io = io.listen(app);
app.listen(80);

function Connection (nick, socket) {
	this.nick = nick;
	this.socket = socket;
}

app.get('/', function (req, res) {
	res.sendfile(__dirname + "/index.html");
});

io.sockets.on('connection', function (socket) {
	var onlinelist = function() {
		list = [];
		for (var id in io.sockets.in('online').sockets) {
			s = io.sockets.in('online').sockets[id]
			s.get('nick', function (err, nick) {
				list.push(nick);
			});
		}
		return list;
	}

	socket.on('set nick', function(nick) {
		socket.join('online');
		socket.set('nick', nick, function () {
			socket.emit('ready', {online: onlinelist()});
		});
	});
 
	socket.on('private msg', function (msg) {
		socket.get('nick', function(err, nick) {
			console.log("[private] " + nick.name + " :",  msg);
		});
	});
		
	socket.on('disconnect', function () {
		console.log(socket + "disconnected");
	});
});


