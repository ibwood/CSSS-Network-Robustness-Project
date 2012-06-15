import GrowthRule

class Scheduler():
	def __init__(self, runtype):
		self.rulelist = []		
		if runtype == "sequential":
			self.r = self.run_sequential

	def add_rule(self, rule):
		self.rulelist.append(rule)

	def set_new_network(self, net):
		for rule in self.rulelist:
			rule.set_new_network(net)

	def run_sequential(self, steps, stepsize):
		for step in range(0, steps):
			for rule in self.rulelist:
				rule.run(stepsize)

	def run(self, steps, stepsize):
		self.r(steps, stepsize)
