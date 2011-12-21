import socket
import os
import httplib
import urllib
import sys

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
	
	print is_valid
	
