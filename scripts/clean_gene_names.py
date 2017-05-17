from config import *
import os

print printAllArgs()

f = open(PATH_TO_UPLOAD+getGenomeFileName(),'r')
out = open(PATH_TO_UPLOAD+getGenomeFileName()+"_clean.fa",'w')

count = 0
for l in f:
	if(l.startswith('>')):
		count+=1
		out.write('>gene'+str(count)+'\n')
	else:
		out.write(l)
out.close()

fullName = PATH_TO_UPLOAD+getGenomeFileName()
indexOfEnd = fullName.rfind('.')
if indexOfEnd == -1:
	indexOfEnd = len(fullName)-1
fullName = fullName[:indexOfEnd+1] + '.fa'
os.system('mv '+PATH_TO_UPLOAD+getGenomeFileName()+"_clean.fa "+ fullName)