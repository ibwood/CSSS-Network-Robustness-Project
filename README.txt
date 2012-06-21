python ControllerBAandClustering.py graphs/ 1 3 10000 1 0 random .1 1000 3 1 .2 0 1
path // in above example: graph/ - this will put it in the graphs folder
id # in prefix rid#_ // in above example: 1 - this will give the gml file a prefix with the run id 
number_seed # in prefix s#_ // in above example: 3 - this will start the graph with a cycle of 3 nodes
init_growth_num # in prefix ig#_ // in the above example: 10000 - this will grow the graph to 10000 nodes in the beginning
init_m_ba_turn # in prefix imbt#_ // in the above example: 1 - this will let the initial growth BA turn only grow 1 edge before checking clustering
init_lambda # in prefix il#_ // in the above example: 0 - this sets the initial growth lambda to 0
attack_type # in prefix at#_ // in the above example: random - this sets the attack type to random (none will not have an attack, anything else will set it to high_degree)
attack_percent # in prefix ap#_ // in the above example .1 - this sets the number of nodes of the graph removed per attack to .1
growth_num # in prefix gn#_ // in the above example 1000 - this grows 1000 nodes back per turns
mtotal # in prefix mt#_ // in the above example 3 - this means that three edges are added when the network grows by one node
m_ba_turn # in prefix mbt#_ // in the above example 1 - this means that each ba turn will only grow one edge before allowing clustering
p # in prefix p#_ // in the above example .2 - this means that there is a .2 chance that a clustering edge will be added instead of a preferential attachment edge
lambda # in prefix l#_ // in the above example 0 - this sets the BA lambda to 0
number_of_turns #in prefix nt#_ // in the above example 1 - this is the number of turns beyond the initial that the grow-attack cycle will run.



