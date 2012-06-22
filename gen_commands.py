init_growth = 10000
command_list= []
for i in range(0, 10):
	for a in range(0, 2):
		a = a * .02
		regrowth = init_growth*a
		for l in range(0, 2):
			l = l * .1
			for p in range(0, 2):
				p = p * .1
				for j in ["random", "degree"]:
					command_list.append("python ControllerBAandClustering.py graphs/ "+str(i)+" 3 "+ str(init_growth)+" 1 "+str(l)+ " "+ j +" "+ str(a) + " "+ str(regrowth)+" 3 1 "+str(p)+" "+str(l)+ " 10")

print(command_list)
print(len(command_list))
