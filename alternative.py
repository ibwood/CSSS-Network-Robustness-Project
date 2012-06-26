import networkx as nx
from memGraph import *
import SeqScheduler
import GrowthRuleBA
from SchedulerBAClustering import *
from GrowthRuleClustering import *
from AttackRuleRandom import *
from AttackRuleHighDegree import *
from WriteRule import *
import datetime
import sys

class Controller(object):
	def __init__(self):
		self.sched = SeqScheduler.SeqScheduler("sequential")
		self.clusteringsched = None
		self.graphs = []

	def addClusteringSched(self, m, p):
		self.clusteringsched = SchedulerBAClustering(m, p)
		self.sched.add_rule(self.clusteringsched)
	def addWriteRule(self, prefix):
		wr = WriteRule(None, prefix)
		self.sched.add_rule(wr)
	def addBARule(self, m, l):
		gba = GrowthRuleBA.GrowthRuleBA(None, m, l)
		self.clusteringsched.add_rule(gba, "BA")
	def addRandAttackRule(self, per):
		ra = AttackRuleRandom(None, per)
		self.sched.add_rule(ra)
	def addHighDegreeAttackRule(self, per):
		rh = AttackRuleHighDegree(None, per)
		self.sched.add_rule(rh)
	def replaceBARule(self, m, l):
		g = self.graphs[-1]
		gba = GrowthRuleBA.GrowthRuleBA(g, m, l)
		self.clusteringsched.add_rule(gba, "BA")
	def addClusteringRule(self):
		gcr = GrowthRuleClustering(None)
		self.clusteringsched.add_rule(gcr, "Clustering")
	def runFresh(self, cyclenodes= 0, steps = 0, stepsize = 0, out="hello.gml"):
		if cyclenodes != 0:
			g = nx.cycle_graph(cyclenodes, create_using=memGraph())
		else:
			g = nx.empty_graph(create_using=memGraph())
		self.graphs.append(g)
		self.sched.set_new_network(g)
		self.run(steps, stepsize)
		#nx.write_gml(g, out)
	def run(self, steps = 0, stepsize = 0):
		g = self.graphs[-1]
		dt = datetime.datetime.now()
		self.sched.run(steps, stepsize)
		
		#gba = self.clusteringsched.rulelist[0]
		#sumiter = 0
		#for i in gba.iterations:
		#	sumiter += i
		#sumiter = float(sumiter)/float(len(gba.iterations))
		#print("Average Iterations: "+str(sumiter))

if __name__ == "__main__":
	filename = sys.argv[1]
	f = open(filename, "r")
	
	for line in f:
		args = line.split()
		pathprefix = args[0]
		rid = args[1]
		number_seed = int(args[2]) # in prefix s#_
		init_growth_num = int(args[3]) # in prefix ig#_
		#init_mtotal = sys.argv[5] # in prefix imt#_
		init_m_ba_turn = int(args[4]) # in prefix imbt#_
		#init_p = sys.argv[7] # in prefix ip#_
		init_lambda = float(args[5]) # in prefix il#_
		attack_type = args[6] # in prefix at#_
		attack_percent = float(args[7]) # in prefix ap#_
		growth_num = int(args[8]) # in prefix gn#_
		mtotal = int(args[9]) # in prefix mt#_
		m_ba_turn = int(args[10]) # in prefix mbt#_
		p = float(args[11]) # in prefix p#_
		lamb = float(args[12]) # in prefix l#_
		number_of_turns = int(args[13]) #in prefix nt#_
		
		prefix = pathprefix + \
			"rid"+str(rid)+"_"+ \
			"s"+str(number_seed)+"_"+ \
			"ig"+str(init_growth_num)+"_"+ \
			"imbt"+str(init_m_ba_turn)+"_"+\
			"il"+str(init_lambda)+"_"+\
			"at"+str(attack_type)+"_"+\
			"ap"+str(attack_percent)+"_"+\
			"gn"+str(growth_num)+"_"+\
			"mt"+str(mtotal)+"_"+\
			"mbt"+str(m_ba_turn)+"_"+\
			"p"+str(p)+"_"+\
			"l"+str(lamb)+"_"+\
			"nt"+str(number_of_turns)+"_"
			#"imt"+str(init_mtotal)+"_"+\
			#"ip"+str(init_ip)+"_"+\
		c = Controller()
		c.addClusteringSched(mtotal, p)
		c.addBARule(init_m_ba_turn, init_lambda)
		c.addClusteringRule()
		c.addWriteRule(prefix+"g") #g for grow
		if attack_type == "random":
			c.addRandAttackRule(attack_percent)
		elif attack_type == "none":
			pass
		else:
			c.addHighDegreeAttackRule(attack_percent)
		c.addWriteRule(prefix+"a") #a for attack
		ign = init_growth_num - number_seed 
		c.runFresh(number_seed, 1, ign)
		c.replaceBARule(m_ba_turn, lamb)
		c.run(number_of_turns, growth_num)
