from random import *
from math import log10
import time

class Investment(object):
	"""docstring for Investment"""
	def __init__(self, money, cut_rate, payoff_rate, risk_rate, N, Q, 
			down_or_compromised, services, risk_aversion):
		super(Investment, self).__init__()
		self.money = float(money)
		self.cut_rate = float(cut_rate)
		self.payoff_rate = float(payoff_rate)
		self.risk_rate = float(risk_rate)
		self.N = float(N)
		self.Q = float(Q)
		self.down_or_compromised = float(down_or_compromised)
		self.services = float(services)
		self.risk_aversion = float(risk_aversion)

	def __eq__(self, other) : 
	        return other != None and self.expected_return_ratio() == other.expected_return_ratio() 
	
	def risk(self):
		"""Dummy function"""
		first = self.risk_rate * self.money/10
		# print first
		second = 0.5*((self.N-700)/(300+abs(self.N-700))+1)
		# print second
		third = 0.5*((self.Q-1500)/(300+abs(self.Q-1500))+1)
		# print third
		return (first + second + third)/3
		
	def running_ratio(self):
		return (self.services - self.down_or_compromised)/self.services
		
	def expected_return_ratio(self):
		if self.payoff() == 0:
			return 0
		return self.expected_return()/self.payoff()
	
	def expected_return(self):
		return self.payoff()*(1-self.risk())*self.running_ratio()
				
	def payoff(self):
		if self.payoff_rate == 0:
			return 0
		return (self.money - self.cut())*self.payoff_rate	
		
	def cut(self):
		return self.money*self.cut_rate
			
	def doit(self):
		return self.expected_return_ratio() >= self.risk_aversion


class PreprocessInvestment(object):
	"""docstring for Preprocess"""
	def __init__(self, money, cut_rate, payoff_rate, risk_rate, N, Q, 
			down_or_compromised, services, risk_aversion):
		super(PreprocessInvestment, self).__init__()
		self.money = money
		self.cut_rate = cut_rate
		self.payoff_rate = payoff_rate
		self.risk_rate = risk_rate
		self.N = N
		self.Q = Q
		self.down_or_compromised = down_or_compromised
		self.services = services
		self.risk_aversion = risk_aversion
		self.alternatives = []

	def calculate_alternatives(self):
		"""docstring for calculate_alternatives"""
		if len(self.alternatives) > 0:
			return self.alternatives
		
		for i in range(1,min(self.money+1,100),1):
			inv = Investment(i, self.cut_rate, self.payoff_rate, self.risk_rate, self.N, self.Q,
					self.down_or_compromised, self.services, self.risk_aversion)
			if (inv.doit()):
				self.alternatives.append(inv)
		if len(self.alternatives) == 0:
			self.alternatives.append(Investment(0, self.cut_rate, self.payoff_rate, self.risk_rate, self.N, self.Q,
					self.down_or_compromised, self.services, self.risk_aversion))
		return self.alternatives

	def best(self):
		"""docstring for best"""
		self.calculate_alternatives()
		if len(self.alternatives) == 0:
			return []
		return [max(self.alternatives)]
		
class Stock(object):
	"""docstring for Stock"""
	def __init__(self, team, exploit, potentials, current_points=0):
		super(Stock, self).__init__()
		self.team = team
		self.exploit = exploit
		self.potentials = potentials
		self.current_points = current_points
		
	def __eq__(self, other):
		return self.team == other.team and self.service == other.service

class SimplePortfolio(object):
	"""docstring for InvestmentAnalysis"""
	def __init__(self, money, stocks = []):
		super(SimplePortfolio, self).__init__()
		self.money = money
		self.stocks = stocks
	
	def add_stock(self, stock):
		"""docstring for add_stock"""
		self.stocks.append(stock)
	
	def portfolio(self):
		"""docstring for portfolio: think we should try to do a optimization of some kind here"""
		money = self.money
		any_changes = True
		portfolio = {}
		while (money > 0 and any_changes):
			any_changes = False
			max = 0
			inv = None
			team = ""
			used_stocks = []
			potential_stock = None
			for stock in self.stocks:
				alternatives = stock.potentials.calculate_alternatives()
				for invest in alternatives:
					if (max <= invest.expected_return() and 
					money >= invest.money and 
					not (portfolio.has_key((stock.team.name, stock.exploit.service, stock.exploit.flag)) and
					portfolio[(stock.team.name, stock.exploit.service, stock.exploit.flag)] >= max)):
						max = invest.expected_return()
						inv = invest
						team = stock.team
						potential_stock = stock
			
			if potential_stock != None:
				used_stocks.append(potential_stock)
				portfolio[(potential_stock.team.name, 
						  potential_stock.exploit.service, potential_stock.exploit.flag)] = inv.money
				money = money - inv.money
				any_changes = True
		
		unused_stocks = []
		for stock in self.stocks:
			for used_stock in used_stocks:
				if stock != used_stock:
					unused_stocks.append(stock)
		
		for unused_stock in unused_stocks:
			investment = stock.potentials.alternatives[0]
			investment.money = 0
			if portfolio.has_key((unused_stock.team.name, unused_stock.exploit.service, unused_stock.exploit.flag)):
				continue
			portfolio[(stock.team.name, stock.exploit.service, stock.exploit.flag)] = 0
		
		return portfolio
		

		
		
# Testing SimplePortfolio
# port = SimplePortfolio(5000)
# pf = port.portfolio()
# print pf
		

# Just to see if everything works... Investment
# inv = Investment(money=10, 
# 				cut_rate = 0.1, 
# 				payoff_rate= 0.8, 
# 				risk_rate = 0.3, 
# 				N = 800, 
# 				Q = 45000,
# 				down_or_compromised = 0, 
# 				services = 10, 
# 				risk_aversion = 0.5)
# print "Money invested         : %f" % inv.money
# print "Risk                   : %f" % inv.risk()
# print "Running Services Ratio : %f" % inv.running_ratio()
# print "Actual Return          : %f" % inv.payoff()
# print "Expected Return        : %f" % inv.expected_return()
# print "     and Ratio         : %f" % inv.expected_return_ratio()
# print "Risk Aversion          : %f" % inv.risk_aversion
# print "Worth it?              : %r" % inv.doit()



