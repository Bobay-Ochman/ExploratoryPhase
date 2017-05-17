from config import *
from mailMessage import *
import os
import sys

print "--- making folders"

# make folders
try:
	os.system('mkdir '+PATH_TO_UPLOAD+'out')
except OSError as e:
	print e


remArgs = ' '+sys.argv[1]+' '+sys.argv[2]+' '+sys.argv[3]+' '

print "--- cleaning the names of the genes"
os.system('python '+PATH_TO_ME + 'scripts/' + 'clean_gene_names.py '+remArgs + ' &> '+PATH_TO_UPLOAD+'out/01_clean.txt')

print "--- Expects just to have a .fa file"
# usearch

sendEmail("We've started your analysis and will be emailing you periodically to keep you updated on how it is going.")

print "--- usearch"
os.system('python '+ PATH_TO_ME + 'scripts/' + 'usearch_global.py'+remArgs+ ' &> '+PATH_TO_UPLOAD+'out/02_u_global.txt')

print "--- candidate"
os.system('python '+ PATH_TO_ME + 'scripts/' + 'candidate.py'+remArgs+ ' &> '+PATH_TO_UPLOAD+'out/03_candidate.txt')

print "--- mailing!"
os.system('python '+ PATH_TO_ME + 'scripts/' + 'mail_results.py'+remArgs+ ' &> '+PATH_TO_UPLOAD+'out/04_mail.txt')

quit()
