from scipy import ones, exp, zeros
from constants import imp0
from pylab import plot, show
def getParams():
	print ''
	params = {}
	#would like to make text file simpler but works in dictionary sytanx for now
	with open('myfile.txt','r') as inf:
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

	E = zeros(tMax)
	H = zeros(tMax)

	#note, this is not TFSF technically
	if (kind == 'g') and (tfsf == True):
		dt = 0
		for t in range(tMax):
			#E[t] = exp(-(t+0.5-(-0.5)-30) * (t+0.5-(-0.5)-30) / 100.0)
			#H[t] = -1*exp(-(t-30) * (t-30) / 100.0) / imp0
			E[t] =    height*exp(-(float(t - offset - (-0.5) + 0.5)*(t-offset- (-0.5) + 0.5)/width/width))
			H[t] = -1*height*exp(-(float(t - offset)*(t-offset)/width/width))/imp0
		print 'TFSF source created successfully'
		#plot(E)
		#plot(-1*H)
		show()
		return [E,H]


