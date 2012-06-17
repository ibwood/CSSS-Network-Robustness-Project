import networkx as nx
import memGraph
import SeqScheduler
import GrowthRuleBA
import datetime

class Controller(object):
	def __init__(self):
		self.sched = SeqScheduler.SeqScheduler("sequential_nodes")
		self.graphs = []

	def addBARule(self, m, l):
		gba = GrowthRuleBA.GrowthRuleBA(None, m, l)
		self.sched.add_rule(gba)
		
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
		print(datetime.datetime.now()-dt)
		nx.write_gml(g, out)

if __name__ == "__main__":
	init = 2	
	n = 9998	
	m = 2
	lam = 0
	outputfile = "graphs/hello.gml"

	c = Controller()
	c.addBARule(m, lam)
	c.runFresh(init, 1, n, outputfile)
