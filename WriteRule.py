import networkx as nx
from Rule import *
class WriteRule(Rule):
	def __init__(self, net, prefix, start=0):
		self.net = net		
		self.prefix = prefix
		self.index = start
	def run(self, n, **args):
		nx.write_gml(self.net, self.prefix+str(self.index)+".gml")
		self.index += 1
	def run_nodes(self, nodes, **args):
		print "Must Implement run_nodes!"
	def set_new_network(self, net):
		self.net = net
