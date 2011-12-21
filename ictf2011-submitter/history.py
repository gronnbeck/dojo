import pickle
import investment
import time
from random import *

class Team(object):
	"""docstring for History"""
	def __init__(self, name, points=0, transfer_history = 0, exploits=[]):
		super(Team, self).__init__()
		self.name = name
		self.transfer_history = transfer_history
		self.exploits = exploits
		self.points = points
	
	def transfer(self, amount):
		transfer_history = transfer_history + amount
		
	def get_investment(self):
		investments = investment.PreprocessInvestment(
								transfer_history 	= int(history[argv[i+1]]), 
								money			 	= int(argv[i+2]), 
								cut_rate 		 	= float(argv[i+3]), 
								payoff_rate 	 	= float(argv[i+4]), 
								risk_rate			= float(argv[i+5]),
								down_or_compromised = int(argv[i+6]), 
								services 			= int(argv[i+7]), 
								risk_aversion 		= float(argv[i+8])).best()
		return investments[0]
		
class Exploit(object):
	"""docstring for Exploit"""
	def __init__(self, service, flag, cut=0, payoff=1, risk=1, N=0, Q=0):
		super(Exploit, self).__init__()
		self.service = service
		self.flag = flag
		self.cut = cut
		self.payoff = payoff
		self.risk = risk
		self.N = 0
		self.Q = 0
		self.used = False
	
	def __eq__(self, other):
		return (self.service == other.service and self.flag == other.flag)

class History(object):
	"""docstring for History"""
	def __init__(self):
		super(History, self).__init__()
		self.history = {}
		self.file = None
	
	def lock(self, filename):
		try:
			self.file = open(filename, "r")
			try:
				self.history = pickle.load(self.file)
			except EOFError as e:
				print "File was empty. Nothing to load"
		except IOError as e:
			print "File not found."
	
	def unlock(self):
		self.file.close()
		
	def load(self, filename):
		self.lock(filename)
		self.file.close()
		
	def save_and_unlock(self, filename):
		self.save(filename)
		self.unlock()
		
	def save(self, filename):
		self.file = open(filename, "w")
		pickle.dump(self.history, self.file)
		
	
	def portfolio(self, money, down_or_compromised, service, risk_aversion):
		portfolio = investment.SimplePortfolio(money, stocks = [])
		for (name, team) in self.history.items():
			for exploit in team.exploits:
				stock = investment.Stock(
						team		   =  team,
						exploit 	   =  exploit,
						current_points =  team.points,
						potentials	   =  investment.PreprocessInvestment(  money,
																			exploit.cut,
																			exploit.payoff,
																			exploit.risk,
																			exploit.N,
																			exploit.Q,
																			down_or_compromised,
																			service,
																			risk_aversion))
				portfolio.add_stock(stock)
		return portfolio.portfolio()
		
	def all_potential_investments(self, money, down_or_compromised, services, risk_aversion):
		options = {}
		for (key, team) in self.history.items():
			for exploit in team.exploits:
				options[key] = investment.PreprocessInvestment(
									money, 
									exploit.cut, 
									exploit.payoff, 
									exploit.risk, 
									team.transfer_history,
									down_or_compromised, 
									services, 
									risk_aversion).best()

		return options	

# -
# history = History()
# print "RISK AVERSION: %f" % (float(aversion)/100)
# team1 = Team(name="Omega", exploits=[])
# team1.exploits.append(Exploit(service="first", flag="hello", cut=0.1, payoff=0.8, risk=0.15))
# history.history[team1.name] = team1
# 
# team2 = Team(name="Alpha", exploits=[])
# team2.exploits.append(Exploit(service="second", flag="world", cut=0.1, payoff=0.9, risk=0.2))
# history.history[team2.name] = team2
# 
# print history.portfolio(1000, 0, 10, float(aversion)/100)
# -
		
# -
"""
history = History()
for i in range(0,60):
	team = Team(name=str(randint(0, 1000000)), exploits=[])
	for i in range(0,12):
		team.exploits.append(Exploit(service=str(randint(0, 1000000)) , flag=str(randint(0, 1000000)), cut=random(), payoff=random(), risk=random()))
	history.history[team.name] = team
portfolio =  history.portfolio(1000, 0, 10, 0.9)
# print portfolio
#print portfolio.keys()[0]
#print portfolio.keys()[0][2]
# - """