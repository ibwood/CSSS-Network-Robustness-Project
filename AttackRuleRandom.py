from memGraph import *
from Rule import *
import networkx as nx
import math
import random

class AttackRuleRandom(Rule):
	def __init__(self, net, percent):
		self.net = net
		self.percent = percent
	def run(self, n, **args):
		N = self.net.number_of_nodes()
		num_to_rem = int(math.ceil(N*self.percent))
		nodes_to_rem = []
		#print self.net.degree()
		for i in range(0, num_to_rem):
			choice = random.choice(self.net.node.keys())
			#print(self.net.degree(choice))
			self.net.remove_node(choice)
		print ("Removed "+str(num_to_rem) + " random nodes")
	def run_nodes(self, nodes, **args):
		print "Must Implement run_nodes!"
	def set_new_network(self, net):
		self.net = net
