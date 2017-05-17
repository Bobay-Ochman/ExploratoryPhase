from config import *
import os


timeStamp = '1'
markers=os.listdir('../markers/')
testGenomes = os.listdir('../uploads/'+timeStamp)
testGenome = testGenomes[0]


nb=0
for hmm in markers:
	if hmm.endswith('.txt'):
		nb+=1
		print hmm,' ',nb ,'/44'
		command = PATH_TO_USEARCH + ' -global -query '+PATH_TO_ME+'/uploads/'+timeStamp+'/'+testGenome+'   -db  '+PATH_TO_ME+'/markers/' + hmm + '  -id 0.7 -blast6out '+PATH_TO_ME+'/uploads/'+timeStamp+'/'+testGenome+'_' + hmm + '.out'
		print command
		os.system(command)