#!/usr/bin/env python
import sys
import os
from history import * 
import asyncore
import socket
import time
from threading import Thread
import json
from flag_sender import *

gamestate_addr = ('10.13.202.3', 55555) # we will listen on port 55555 for game state

game_state = None
log_filename = "main_log.txt"
log_file = None
current_state_filename = "current_state.txt"
current_state_file = None

current_state_str = ""

class GameStateHandler(asyncore.dispatcher_with_send):
	
	def handle_read(self):
		global game_state, current_state_str
		
		data = self.recv(1032768)
		
		current_state_str += data
		
		if data == "" or data[-1] == "\n": # reached end of state
			
			try:
				game_state = json.loads(current_state_str)
			except ValueError, e:
				print e, ":"
				#print repr(data)
				log("ERROR: Invalid state received (or incomplete?)")
			
				print current_state_str
				return
			
			current_state_str = ""
			
			log("got new state. tick:" + str(game_state['tick']))
			#print json.dumps(game_state, indent=2)
			current_state_file.seek(0)
			current_state_file.truncate()
			current_state_file.write(time.strftime("This game state pushed to us at: %H:%M:%S\n", time.localtime()))
			current_state_file.write(json.dumps(game_state, indent=2))
			current_state_file.flush()
		
class GameStateListener(asyncore.dispatcher):

	def __init__(self, addr):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.set_reuse_addr()
		self.bind(addr)
		self.listen(5)
		
	def handle_accept(self):
		pair = self.accept()
		if pair is None:
			pass
		else:
			sock, addr = pair
			print 'Incoming connection from %s' % repr(addr)
			handler = GameStateHandler(sock)


def log(msg):
	logmsg = "%s - %s" % (time.strftime("%H:%M:%S", time.localtime()), msg)
	print logmsg
	logfile.write(logmsg + "\n")
	logfile.flush()

if __name__ == "__main__":

	logfile = open(log_filename, "a")
	current_state_file = open(current_state_filename, "w")

	game_state_listener = GameStateListener(gamestate_addr)
	
	# One thread will loop waiting to get game state
	Thread(target=asyncore.loop).start()
	
	#asyncore.loop()  # COMMENT THIS OUT, AND UNCOMMENT ABOVE 
		
	while True:
		
		if not game_state: 
			time.sleep(10)
			continue
	
		filename = "history.dat"
	
		# fetch exploits from history
		current_exploits = []
		history = History()
		history.lock(filename)
		portfolio = []
		for (name, team) in history.history.items():
			for exploit in team.exploits:
				# add c, r, p to exploits (merge)
				print int(exploit.flag[3:7]) 
				if (int(exploit.flag[3:7]) != int(game_state["tick"]) and not exploit.used):
					team.exploits.remove(exploit)
					continue
				exploit.cut = float(game_state['services'][exploit.service]['C']) / 100
				exploit.risk = float(game_state['services'][exploit.service]['R']) / 100
				exploit.payoff = float(game_state['services'][exploit.service]['P']) / 100
				
				if not game_state["teams"]["Team Omega"]["N"].has_key(exploit.service):
					exploit.Q = 0
				else:
					exploit.Q = game_state["teams"]["Team Omega"]["N"][exploit.service]
					
				if not game_state["teams"]["Team Omega"]["Q"].has_key(exploit.service):
					exploit.N = 0
				else:
					exploit.N = game_state["teams"]["Team Omega"]["Q"][team.name]
				exploit.used = True
					
				# current_exploits.append(exploit)
				
		
		# tell history to calculate portfolio (it returns it)
		portfolio = history.portfolio(money = game_state["teams"]["Team Omega"]["money"],
									  down_or_compromised = 10-len(game_state["teams"]["Team Omega"]["services_up_last_tick"]),
									  service = 10,
									  risk_aversion = 0.5)
	
		# send flags
		for (key, amount) in portfolio.items():
			send_flag(flag=key[2],amount=min(70, int(amount))) # AMOUNT
		
		num_flags = len(portfolio)
		if num_flags == 0:
			print "no flags to send"
		else:
			print "sent %d flags" % len(portfolio)
		
		# need to find a way to choose which exploits to snitch on..
	
	
		# remove exploit from each team exploit list
		for (name, team) in history.history.items():
			team.exploits = []
				
	
		#history.load_history()
		#log(history.history['team1'].name)
		# print history.portfolio(500, 0, 10, 0.1)
		# print history.all_potential_investments(500, 0, 10, 0.1)
		history.save_and_unlock(filename)
	
		time.sleep(10)