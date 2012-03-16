var net = require('net');
var client = net.createConnection(6667, "205.188.234.121");
var connecting = false;
var connected = false;
client.on('connect', function(){
	console.log("connected");
	connecting = true;
});

client.on('data', function(data){
	console.log(""+data);
	if (connecting){
		client.write("USER gronnbeckBot gronnbeckBot gronnbeckBot :Roger Per\n")
		client.write("NICK kenbot\n");
		
		connecting = false;
		connected = true;
		//client.write("JOIN #PR")
	}
	if (connected){
		client.write("JOIN #PR\n");
	}
});

