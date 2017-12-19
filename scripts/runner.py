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

try:
	f = open(PATH_TO_UPLOAD+'cleaning_errors.txt',"r")
	emailMessage = 'The file you have uploaded appears to not be in the proper format. Please be sure to upload a multi-FASTA file of the protein-coding genes of the genome. An error log is listed below.\n\nLog:\n'
	emailMessage += "".join(f.readlines())
	sendEmail(emailMessage)
	os.system("echo quitting, going home > out/11_stopping.txt")
	goHome()
except:
	sendEmail("We've started your analysis and will email you at this address upon completion.")

print "--- usearch"
os.system('python '+ PATH_TO_ME + 'scripts/' + 'usearch_global.py'+remArgs+ ' &> '+PATH_TO_UPLOAD+'out/02_u_global.txt')

print "--- candidate"
os.system('python '+ PATH_TO_ME + 'scripts/' + 'candidate.py'+remArgs+ ' &> '+PATH_TO_UPLOAD+'out/03_candidate.txt')

print "--- mailing!"
os.system('python '+ PATH_TO_ME + 'scripts/' + 'mail_results.py'+remArgs+ ' &> '+PATH_TO_UPLOAD+'out/04_mail.txt')

quit()
