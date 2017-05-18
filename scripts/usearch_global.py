from config import *
import os


timeStamp = getTimeStamp()
testGenome = getGenomeFileName()
markers=os.listdir('../markers/')

nb=0
for hmm in markers:
	if hmm.endswith('.txt'):
		nb+=1
		print hmm,' ',nb ,'/44'
		command = PATH_TO_USEARCH + ' -usearch_global '+PATH_TO_UPLOAD+'/'+testGenome+'   -db  '+PATH_TO_ME+'/markers/' + hmm + '  -id 0.7 -strand plus -blast6out '+PATH_TO_UPLOAD+'/'+testGenome+'_' + hmm + '.out'
		print command
		os.system(command)