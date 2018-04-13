import itertools

l = 4
n = 16
def rt(c,d):
	opCount = 0
	x = c
	opCount += 1
	
	for j in range(0,l):
		opCount += 1
		
		x = x*x
		opCount += 2
		
		iter = 0
		while(n <= x):
			x = x - n
			iter += 1
		opCount += (2*iter + 1)
		
		opCount += 1
		if(d[j] == 1):
			x = x*c
			opCount += 2

			iter = 0
			while(n <= x):
				x = x - n
				iter += 1
			opCount += (2*iter + 1)
	
	#for loop failing -- this should be here
	#opCount += 1
	return opCount

def runner(reps):
	keys = map(list, itertools.product([0,1], repeat = reps))
	for d in keys:
		print "d = " + str(d)
		q = 1
		if(rt(q,d) != 21):
			continue
		for c in range(0,16):
			print str(c) + " , " + str(rt(c,d))
		print ""

runner(4)