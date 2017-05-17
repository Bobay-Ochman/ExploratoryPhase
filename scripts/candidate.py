from config import *
import os

output=os.listdir(PATH_TO_UPLOAD)

profiles=[]
best,all={},{}
for out in output:
	if out.startswith(getGenomeFileName()+'_'):
		profiles.append(out)
		best[out]=['NA',0]
		all[out]={}
		f=open(PATH_TO_UPLOAD+ out ,'r')
		for l in f:
			a=l.strip('\n').split('\t')
			match = a[1]
			sp = match.split(' ')[0]
			score=float(a[2])
			if all[out].has_key(sp):
				if score > all[out][sp]:
					all[out][sp]=score
			else:
				all[out][sp]=score
			#print sp,' ',score
			if score > best[out][1]:
				best[out] = [sp,score]
		f.close()

species=[]
for out in best:
	sp = best[out][0]
	if sp not in species:
		species.append(sp)


markers={}
f=open(PATH_TO_ME+'/markers/number_markers.txt','r')
for l in f:
	a=l.strip('\n').split('\t')
	markers[a[0]] = a[1]

f.close()

fileOut = open(PATH_TO_UPLOAD+'FinalResults.txt','w')

print 'We have ',len(species),' candidate(s) for you:\n'
multiple=[]
candidate=['none',0,0]
MAX=0
for sp in species:
	tmp=[]
	for out in profiles:
		try:
			tmp.append(all[out][sp])
		except KeyError:
			pass
	if len(tmp) > MAX:
		MAX=len(tmp)
	if len(tmp) > 0:
		if median(tmp) >= 98 and len(tmp) >= 10:
			multiple.append(sp)
		message = ""+sp+' matched '+str(len(tmp))+ ' profiles over '+ markers[sp]+' for this species, Median identify score= '+str(median(tmp))+'%'
		print message
		fileOut.write(message+'\n')
		if median(tmp) > candidate[1] and len(tmp) >= 10:
			candidate=[sp,median(tmp),len(tmp)]


message = ''
if candidate[1] >= 94 and len(multiple) <= 1:
	message= '\nMost likely species of '+getGenomeFileName()+': '+candidate[0]
elif len(multiple) > 1:
		message= '\nMultiple candidates with >98% identity: '+('\n'.join(multiple))
else:
	message= '\nNo match found for '+getGenomeFileName()+' over 94% identity (but the databank might be incomplete)'

print message
fileOut.write(message)
fileOut.close()















