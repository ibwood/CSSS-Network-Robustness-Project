import os
import shutil

beginn=1
beginm=1 

nr=2 # tradeoff power 
mr=2 # external death

#it is handy to create string variables with the names of your files, so that you only need to change them in one place in the script

name = 'ControllerBAandClustering.py'
directory_name = 'Robustness'
myprogram = 'Robustness'
init_growth = 10000
dirName = "graphs"
#if directory is not there yet, create it    
os.mkdir(dirName)  
for i in range(0, 10):
	for a in range(0, 2):
		a = a * .02
		regrowth = init_growth*a
		for l in range(0, 2):
			l = l * .1
			for p in range(0, 2):
				p = p * .1
				for j in ["random", "degree"]:
					job_name='job_' + str(i) +str(a)+str(l)+str(p)+j 
					f=open(job_name,'w')
					f.write('#PBS -N'+' job_' + myprogram +'_n_'+ str(trade) + '_d_' + str(edeath) + '\n')
					f.write('#PBS -l walltime=20:00:00\n')
					f.write('#PBS -l nodes=1:ppn=1\n')
					f.write('#PBS -j oe\n')
					#f.write('cd Robustness/'+ dirName + '\n')
					#f.write('./' + myprogram + ' ' + str(trade) + ' ' + str(edeath) + '\n')
					f.write('./'+"python ControllerBAandClustering.py graphs/ "+str(i)+" 3 "+ str(init_growth)+" 1 "+str(l)+ " "+ j +" "+ str(a) + " "+ str(regrowth)+" 3 1 "+str(p)+" "+str(l)+ " 10")
                                                                
					f.close()
					os.popen('qsub '+ job_name)
