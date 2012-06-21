from Scheduler import *
import networkx as nx
import datetime
class SeqScheduler(Scheduler):
	def __init__(self, runtype):
		self.rulelist = []
		self.net = None		
		if runtype == "sequential":
			self.r = self.run_sequential
		if runtype == "sequential_nodes":
			self.r = self.run_sequential_nodes
	def add_rule(self, rule):
		self.rulelist.append(rule)

	def set_new_network(self, net):
		self.net = net
		for rule in self.rulelist:
			rule.set_new_network(net)

	def run_sequential_nodes(self, steps, stepsize):
		for step in range(0, steps):
			if step % 5000 == 0:
				print step
			nodes = []
			for n in range(0, stepsize):
				nodes.append(self.net.get_next_index(inc=1))
			for rule in self.rulelist:
				rule.run_nodes(nodes)

	def run_sequential(self, steps, stepsize):
		for step in range(0, steps):
			dt = datetime.datetime.now()
			for rule in self.rulelist:
				rule.run(stepsize)
			print("Edges: "+str(len(self.net.edges())))
			print("Nodes: "+str(len(self.net.node)))
			print("Average Clustering: "+str(nx.average_clustering(self.net)))
			
			print(datetime.datetime.now()-dt)
	def run(self, steps, stepsize):
		self.r(steps, stepsize)
	
	def run_nodes(self, nodes):
		for node in nodes:
			for rule in self.rulelist:
				rule.run_nodes(node)
