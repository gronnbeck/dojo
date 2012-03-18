import socket
import json

HOST = 'localhost'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = { 'cmd': 'push',
		 'push': { 
		 	'file': 'random.txt',
			'data': 'random data'
		  } 
	   }
s.sendall(json.dumps(data))
print  s.recv(50)
p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
p.connect((HOST, 8889))
p.sendall("Hello world")
p.close()
s.close()
print "Done"

