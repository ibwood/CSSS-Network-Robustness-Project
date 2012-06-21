from memGraph import *
from Rule import *
import networkx as nx
import math

class AttackRuleHighDegree(Rule):
	def __init__(self, net, percent):
		self.net = net
		self.percent = percent
	def cmp(self, x, y):
		return self.net.deg[x] - self.net.deg[y]
	def run(self, n, **args):
		num_to_rem = int(math.ceil(self.net.number_of_nodes()*self.percent))
		sortedlist = self.net.node.keys()
		sortedlist.sort(cmp=self.cmp, reverse=True)
		self.net.remove_nodes_from(sortedlist[0:num_to_rem])
		print("Removed "+str(num_to_rem)+" highest degree nodes")
	def run_nodes(self, nodes, **args):
		print "Must Implement run_nodes!"
	def set_new_network(self, net):
		self.net = net
