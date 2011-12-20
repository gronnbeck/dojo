function ChatProfile(socket) {
	this.socket = socket;
	this.username; 
}
var net = require('net')
var users = [];
var sockets = [];

var server = net.createServer(function(socket){
	var username = "";
	var userProfile = new ChatProfile(socket);
	
	socket.on('connect', function(){
		userProfile.socket.write("Enter username: ")
		
	});
	socket.on('data', function(data){
		if (username == ""){
			// FORMAT USERNAME - remove nextline
			username = data.toString();
			var pos = username.indexOf("\n");
			username = username.substring(0,pos);
			userProfile.username = username;
			
			users.push(userProfile);
			userProfile.socket.write("Welcome " + userProfile.username + "! You are now able to test the chat: \n");
		}
		// [FUNKER IKKE] Kan det være noe med koding av strings mellom node.js og terminalen
		else if (data.toString() == ".list\n"){ 
			for (var i = 0; i < users.length; i++){
				userProfile.socket.write((i+1) + ". " + users[i].username + "\n");
			}
			
		}
		else {
			for (var i = 0; i < users.length; i++){
				if (users[i] == userProfile) continue;
				users[i].socket.write(userProfile.username + ": " + data);
			}
			//socket.write(userProfile.username + ": " + data);
		}
	})
	socket.on('end', function(){
		var i = users.indexOf(userProfile);
		users.splice(i, i+1);
	});
});

server.listen(8000);