from Rule import *
import networkx as nx
import random

class GrowthRuleClustering(Rule):
	def __init__(self, net):
		self.net = net

	def run(self, n):
		print "Must Implement run!"

	def run_nodes(self, nodes, validneighbors):
		resultlist = []
		#print "inside"		
		#print nodes
		#print validneighbors
		#print self.net.neighbors(nodes[0])
		#print self.net.neighbors(validneighbors[0])
		#print "inside"		
		for node in nodes:
			nodeneighs = self.net.neighbors(node)
			list_neighbors = [] #possible connections to find neighbors
			for validnode in validneighbors:
				if validnode in nodeneighs:
					list_neighbors.append(validnode)
			poss_conns = [] #possible new neighbors
			for ln in list_neighbors:
				ln_neighbors = self.net.neighbors(ln)
				for l in ln_neighbors:
					if l not in nodeneighs and l != node:
						poss_conns.append(l)
			
			#print node
			#print validneighbors
			#print poss_conns
			if len(poss_conns) != 0:
				edgeto = (random.choice(poss_conns))
				#print(edgeto)
				self.net.add_edge(node, edgeto)
				resultlist.append(True)
			else:
				resultlist.append(False)
		return resultlist
	def set_new_network(self, net):
		self.net = net
