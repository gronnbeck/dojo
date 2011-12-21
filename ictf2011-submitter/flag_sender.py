import socket
import os
import httplib
import urllib

# might be a HTTP POST .. check planet_lab node code for that

def send_flag(flag, amount):
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("10.13.202.2", 20200))
	s.send(flag + "\t\t")
	s.send(str(amount) + "\n")
	s.close()