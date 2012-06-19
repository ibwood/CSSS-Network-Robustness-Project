import networkx as nx
import memGraph
import SeqScheduler
import GrowthRuleBA
from SchedulerBAClustering import *
from GrowthRuleClustering import *
import datetime

class Controller(object):
	def __init__(self):
		self.sched = SeqScheduler.SeqScheduler("sequential")
		self.clusteringsched = None
		self.graphs = []

	def addClusteringSched(self, m, p):
		self.clusteringsched = SchedulerBAClustering(m, p)
		self.sched.add_rule(self.clusteringsched)

	def addBARule(self, m, l):
		gba = GrowthRuleBA.GrowthRuleBA(None, m, l)
		self.clusteringsched.add_rule(gba, "BA")
	def addClusteringRule(self):
		gcr = GrowthRuleClustering(None)
		self.clusteringsched.add_rule(gcr, "Clustering")
	def runFresh(self, cyclenodes= 0, steps = 0, stepsize = 0, out="hello.gml"):
		if cyclenodes != 0:
			g = nx.cycle_graph(cyclenodes, create_using=memGraph.memGraph())
		else:
			g = nx.empty_graph(create_using=memGraph.memGraph())
		self.graphs.append(g)
		self.sched.set_new_network(g)
		dt = datetime.datetime.now()
		self.sched.run(steps, stepsize)
		print(len(g.edges()))
		print(len(g.node))
		print nx.average_clustering(g)
		gba = self.clusteringsched.rulelist[0]
		sumiter = 0
		for i in gba.iterations:
			sumiter += i
		sumiter = float(sumiter)/float(len(gba.iterations))
		print("Average Iterations: "+str(sumiter))
		print(datetime.datetime.now()-dt)
		nx.write_gml(g, out)

if __name__ == "__main__":
	init = 3	
	n = 19997	
	mtotal = 3
	m = 1
	p = .4
	mt = p * (mtotal-1)
	lam = 0
	outputfile = "graphs/hello.gml"

	print "mt: "+str(mt)
	c = Controller()
	c.addClusteringSched(mtotal, p)
	c.addBARule(m, lam)
	c.addClusteringRule()
	c.runFresh(init, 1, n, outputfile)
