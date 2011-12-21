import socket


def send_flag(flag, amount):
	conn = httplib.HTTPConnection("10.13.2.201", 8082)
	
	conn.request("GET", '/')
	response = conn.getresponse()
	
	data = response.read()
	hidden_str = '<input type=hidden value="'
	i1 = data.find("<input type=hidden value=") + len(hidden_str)
	i2 = data.find('"', i1+1)
	fc =  data[i1:i2]
	
	#print "hidden value:", fc
	
	url = 'http://10.13.2.201:8082/launder?flag=%s&amount=%s&fc=%s' % (flag, str(amount), fc)
	
	params = urllib.urlencode({'flag': flag, 'amount': amount, 'fc': fc})
	#print 'params', params
	headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
	
	conn.request("GET", url, params, headers)
	response = conn.getresponse()
	#print response.status, response.reason
	data = response.read()
	#print data
	
	is_valid = (data.find("invalid flag") == -1)
	
	return is_valid
	
	
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("10.13.202.2", 8080))
s.listen(5)

while True:
	(clientsocket, address) = s.accept()
	data
	while True:
		c = s.recv(1)
		if c == "\n":
			break
		data += c
	
	items = data.split("\t\t")
	
	print items
	send_flag(items[0], items[1])
	
	