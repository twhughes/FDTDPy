from scipy import ones, exp
from numpy import zeros
from constants import imp0
from pylab import plot, show
def getParams():
	print ''
	params = {}
	#would like to make text file simpler but works in dictionary sytanx for now
	with open('input.txt','r') as inf:
		params = eval(inf.read())
	return params

def makeEnv(env, L):
	print 'making environment'
	epsData = env['eps']
	muData = env['mu']
	eps = ones(L)
	mu = ones(L)

	for box, e in epsData:
		eps[box[0]:box[1]] = e

	for box, m in muData:
		mu[box[0]:box[1]] = m

	print 'environment created successfully'

	return [eps, mu]

def makeSource(source, tMax):
	print 'creating source'
	tfsf = source['tfsf']
	width = source['width']
	height = source['height']
	kind = source['type']
	offset = source['offset']

	E = []
	H = []

	#note, this is not TFSF technically
	if (kind == 'g') and (tfsf == True):
		dt = 0
		for t in range(tMax):
			E.append( exp(-(t+0.5-(-0.5)-30) * (t+0.5-(-0.5)-30) / 100.0) )
			H.append(-1.0*exp(-(t-30) * (t-30) / 100.0) / imp0)
		#	E.append(  height*exp(-(float(t - offset + 2.0/3)*(t-offset + 2.0/3)/width/width))
			#H[t] = -1*height*exp(-(float(t - offset)*(t-offset)/width/width))/imp0
		print 'TFSF source created successfully'
		#plot(E)
		#plot(-1*H)
	#	show()
		return [E,H]


