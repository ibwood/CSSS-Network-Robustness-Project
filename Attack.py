import networkx as nx
import random
import datetime
import matplotlib.pyplot as plt
import math

class GrowthRuleBA:
	def barabasi_albert(self, net, n, m, l):
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
			newnode = N
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

gba = GrowthRuleBA()
g = nx.empty_graph()
plt.figure()

Nnodes = 5000
for lam in range(10,11):
        l = lam * 0.1
        gba.barabasi_albert(g, Nnodes, 5, l)
        import networkx.utils as utils

        #plot log-log degree distribution
        deg  = g.degree() # get degrees
        #cumval = list(utils.cumulative_sum(deg.values()))
        val = sorted(set(deg.values())) #values of degrees
        hist = [deg.values().count(x) for x in val] #histogram of degrees

        diam=[]
        for k in range(0,11):

            nodes_to_rem=[random.randint(0,(Nnodes)) for r in xrange(int(0.01 * Nnodes + 1))]
            g.remove_nodes_from(nodes_to_rem)
            diam.append(nx.diameter(g))
        plt.plot(diam, '-ro')

        #logval = []
        #loghist = []
        #for k in range(0,len(val)):
        #        logval.append(math.log(val[k]))
        #       loghist.append(math.log(hist[k]))
        
        
        #plt.plot(logval, loghist,'.', markersize=12, color='red')
        #plt.plot(logval, loghist, hold=True) #,'ro-', markersize=12
        #cumulative_distribution(g.degree())

#plt.xlabel('Log Degree')
#plt.ylabel('Log Number of nodes')
#plt.title('BA network')
#plt.show()
#plt.savefig('BAdeglog.pdf')
plt.show()
plt.savefig('RandnodesAttack.png')

#nx.write_gml(g, "hello.gml")

#print(len(g.edges()))
#print(len(g.node))

