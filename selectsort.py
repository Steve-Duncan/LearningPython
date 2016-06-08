
def selectSort(x):	
	#need to iterate list n-1 times to compare each pair of values
	for n in range (0, len(x)-1):
		#set the initial value of min to the first element of the list
		min = x[n]
		#print "Pass",n
		#print "Starting minimum is",min
		#iterate list for all values for position n and after; so each loop will look at 1 fewer elements
		for i in x[n:]:
			#print "\tIf",i,"<",min,":"
			#check is current value is less than minimum value; if it is, reset the value
			if i < int(min):
				min = i
			#print "New minimum is",min," ;value of n is",n
			#remove the current minimum value from the list
			x.remove(min)
			#and add it back before the nth position (the start of the remaining elements being evaluated)
			x.insert(n,min)
	return x



#import random module for random number generation
import random

#initialize list
sample = []
#populate sample list with random numbers
for i in range (0, 100):
	sample.append(random.randrange(0,10000))


print "Starting list:",sample
print "Sorted list:",selectSort(sample)

