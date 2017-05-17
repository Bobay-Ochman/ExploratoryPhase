import sys


def getTimeStamp():
	return sys.argv[1]

def getGenomeFileName():
    return sys.argv[2]

def getEmail():
    return sys.argv[3]


PATH_TO_USEARCH = '/Users/Admin/Documents/Work/testDataBank/usearch5.2.32_i86osx32'
PATH_TO_ME = '/Users/Admin/Documents/Work/ExploratoryPhase/'
PATH_TO_UPLOAD = PATH_TO_ME+'/uploads/'+getTimeStamp()+'/'


########################################################################
import math

 
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