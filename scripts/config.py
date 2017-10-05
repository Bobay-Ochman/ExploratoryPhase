import sys
import math


def getTimeStamp():
	return sys.argv[1]

def getGenomeFileName():
    return sys.argv[2]

def getEmail():
    return sys.argv[3]

def printAllArgs():
    return str(sys.argv)

curr_dir = '/var/app/current/'

PATH_TO_USEARCH = curr_dir+'efs/progs/usearch8.0.1623_i86linux32'
PATH_TO_ME = curr_dir+'efs/ExploratoryPhase/'
PATH_TO_UPLOAD = curr_dir+'efs/uploads/'+getTimeStamp()+'/'


def getUsername():
    fs = open(curr_dir+'emailCredentials.txt','r')
    lines = fs.readlines()
    return lines[0].strip('\n')


def getPassword():
    fs = open(curr_dir+'emailCredentials.txt','r')
    lines = fs.readlines()
    return lines[1].strip('\n')

########################################################################


def mean( echantillon ) :
    size = len( echantillon )
    moyenne = float(sum( echantillon )) / float(size)
    return moyenne


def stat_variance( echantillon ) :
    n = float(len( echantillon )) # taille
    mq = mean( echantillon )**2
    s = sum( [ x**2 for x in echantillon ] )
    variance = s / n - mq
    return variance


def stat_ecart_type( echantillon ) :
    variance = stat_variance( echantillon )
    ecart_type = math.sqrt( variance )
    return ecart_type

def median( echantillon) :
	echantillon.sort()
	size = len( echantillon )
	if len( echantillon ) % 2 == 0:
		M= float(echantillon[size / 2 - 1] + echantillon[size / 2]) / 2
	else:
		M= echantillon[size / 2]
	return M

########################################################################