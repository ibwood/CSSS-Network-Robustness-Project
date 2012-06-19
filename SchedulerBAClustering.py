from Rule import *
import random

class SchedulerBAClustering(Rule):
	def __init__(self, m, p):
		self.rulelist = [None, None]
		self.net = None	
		self.m = m
		self.p = p

	def run(self, n):
		for i in range(0, n):
			if i % 5000 == 0:
				print i
				self.net.resort()
			node = self.net.get_next_index()
			nodes = self.rulelist[0].run_nodes([node])[0]
			#print nodes				
			bam = len(nodes)		
			#print bam		
			for n in range(0, self.m-bam):
				check = random.random()
				flag = False
				if check < self.p:
					results = self.rulelist[1].run_nodes([node], nodes)
					flag = results[0]				
				#print flag
				if not flag:
					nodes = self.rulelist[0].run_nodes([node])[0]				
	def run_nodes(self, nodes, **args):
		print "Must Implement run_nodes!"

	def set_new_network(self, net):
		self.net = net
		for rule in self.rulelist:
			rule.set_new_network(net)

	def add_rule(self, rule, ruletype = "Clustering"):
		if ruletype == "BA":
			self.rulelist[0] = rule
		elif ruletype == "Clustering":
			self.rulelist[1] = rule
		else:
			raise Exception("Rule must be BA or Clustering")
