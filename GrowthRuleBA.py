import networkx as nx
import memGraph
import random
import datetime
from Rule import *

class GrowthRuleBA(Rule):
	def __init__(self):
		pass

	def __init__(self, network, m, l):
		self.l = l
		self.m = m
		self.net = network
		self.c = Comparator(self.net)
		self.ba = None
		self.decide()
		self.iterations = []

	def decide(self):
		if hasattr(self.net, 'degreesum'):
			self.ba = self.barabasi_albert_internalmemory
		else:
			self.ba = self.barabasi_albert
	
	def set_new_network(self, net):
		self.net = net
		self.decide()
		self.c = Comparator(self.net)

	def run(self, n):
		self.ba(self.net, n, self.m, self.l)

	def run_nodes(self, nodes):
		newnodes = []
		for node in nodes:
			newnodes.append(self.barabasi_albert_addnode(node))
		return newnodes
	def barabasi_albert_addnode(self, newnode):
		net = self.net
		N = net.number_of_nodes()# - net.degree(newnode)
		m = self.m
		l = self.l
		
		degreesum = net.degreesum
		checks = list(net.nodelist)
		if net.has_node(newnode):
			N -= net.deg[newnode] + 1
			checks.remove(newnode)
			for neighbor in net.neighbors(newnode):
				degreesum -= net.deg[neighbor]
				checks.remove(neighbor)
		#checks = sorted(checks, cmp= self.c.cmp, reverse=True)
		links = []
		nodes = []
		denominator = N * l + (1-l)*(degreesum+N)
		flag = True
                iterations = 0
		while(flag):
			#initialize all probabilities for preferential attachment calculations, sorted from least to highest
			p = []
			for j in range(0, m-len(links)):
				p.append(random.random()*denominator)
			p.sort()

			#iterate over nodes in degrees dictionary
			degsum = 0
			examine = p.pop(0)
			#print "before"
			for node in checks:
				iterations += 1
				#print "in"
				#add to degsum until higher than the threshold probability for attachment, only one attachment per node is allowed implicitly
				degsum += l + (1-l) * (net.deg[node]+1)
				if(degsum >= examine):
					#add a link to the list of links to add to the network
					links.append((newnode,node))
					nodes.append(node)
					#update the dictionary of node degrees
					if(len(p) != 0):
						examine = p.pop(0)
					else:
						#print "here"
						break;
			links = list(set(links))
			if len(links) < m:
				flag = True
				#print('here: '+str(len(links)))
			else:
				flag = False
		#add the m preferentially attached edges, this also adds the node
		net.add_edges_from(links)
		self.iterations.append(iterations)
		return nodes

	def barabasi_albert_internalmemory(self, net, n, m, l=0):
		#dt = datetime.datetime.now()
		#initialize a cyclic graph in case net is empty
		if net.node == {}:
			links = []
			for j in range(1,m):
				links.append((j, j-1))
			links.append((0, m-1))
			net.add_edges_from(links)
			n = n-m

		#initialize degreesum, number of nodes, and degrees
		#calculated once here, updated in memory in the loop for better speed
		N = net.number_of_nodes()
		
		#for i in the range from 0 to n nodes to add, add a new node with m links
		for i in range(0,n):
			degreesum = net.degreesum
			if(i != 0 and i % 5000 == 0):
				print ("here:"+str(i))
			newnode = net.get_next_index()
			
			links = []
			
			denominator = N * l + (1-l)*degreesum
			flag = True
			while(flag):
				#initialize all probabilities for preferential attachment calculations, sorted from least to highest
				p = []
				for j in range(0, m-len(links)):
					p.append(random.random()*denominator)
				p.sort()

				#iterate over nodes in degrees dictionary
				degsum = 0
				examine = p.pop(0)
				for node in net.node:
					#add to degsum until higher than the threshold probability for attachment, only one attachment per node is allowed implicitly
					degsum += l + (1-l) * net.deg[node]
					if(degsum >= examine):
						#add a link to the list of links to add to the network
						links.append((newnode,node))
						#update the dictionary of node degrees
						if(len(p) != 0):
							examine = p.pop(0)
						else:
							break;
				links = list(set(links))
				if len(links) < m:
					flag = True
					#print('here: '+str(len(links)))
				else:
					flag = False
			#update N by the added node i, degreesum by 2 * m (each edge is attached at both ends), and the degrees dictionary
			N += 1
			#add the m preferentially attached edges, this also adds the node
			net.add_edges_from(links)
		#print(datetime.datetime.now()-dt)

	def barabasi_albert(self, net, n, m, l = 0):
		dt = datetime.datetime.now()
		#initialize a cyclic graph in case net is empty
		if net.node == {}:
			links = []
			for j in range(1,m):
				links.append((j, j-1))
			links.append((0, m-1))
			net.add_edges_from(links)
			n = n-m

		#initialize degreesum, number of nodes, and degrees
		#calculated once here, updated in memory in the loop for better speed
		degreesum = sum(net.degree().values())
				
		degrees = net.degree()
		N = net.number_of_nodes()
		
		#for i in the range from 0 to n nodes to add, add a new node with m links
		for i in range(0,n):
			if(i % 5000 == 0):
				print (i)
			newnode = N #net.get_next_index()
			links = []
			
			denominator = N * l + (1-l)*degreesum
			flag = True
			while(flag):
				#initialize all probabilities for preferential attachment calculations, sorted from least to highest
				p = []
				for j in range(0, m-len(links)):
					p.append(random.random()*denominator)
				p.sort()

				#iterate over nodes in degrees dictionary
				degsum = 0
				examine = p.pop(0)
				for node in degrees:
					#add to degsum until higher than the threshold probability for attachment, only one attachment per node is allowed implicitly
					degsum += l + (1-l) * degrees[node]
					if(degsum >= examine):
						#add a link to the list of links to add to the network
						links.append((newnode,node))
						#update the dictionary of node degrees
						degrees[node] += 1
						if(len(p) != 0):
							examine = p.pop(0)
						else:
							break;
				links = list(set(links))
				if len(links) < m:
					flag = True
					#print('here: '+str(len(links)))
				else:
					flag = False
			#update N by the added node i, degreesum by 2 * m (each edge is attached at both ends), and the degrees dictionary
			N += 1
			degreesum += 2 * m
			degrees[newnode]= m
			#add the m preferentially attached edges, this also adds the node
			net.add_edges_from(links)
		print(datetime.datetime.now()-dt)
class Comparator(object):
	def __init__(self, net):
		self.net = net
	def cmp(self, x, y):
		return self.net.deg[x] - self.net.deg[y]
