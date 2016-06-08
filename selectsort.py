
#create functions to select sort a list of numbers. The first function finds the minimum value for each iteration of the list
#adds the min value to the start of the array and removes it from later in the array
#the second function finds min and max values, removes them from the list and adds the min to the start of the list and the 
#value to the end of the list.

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

def selectSortMinMax(x):	
	#need to iterate list n-1 times to compare each pair of values
	for n in range (0, len(x)-1):
		#set the initial value of min to the first element of the list
		min = x[n]
		max = x[n]
		#print "Pass",n
		#print "Starting minimum is",min
		#iterate list for all values for position n and after; so each loop will look at 1 fewer elements
		for i in x[n:]:
			#print "\tIf",i,"<",min,":"
			#check is current value is less than minimum value; if it is, reset the value
			if i < int(min):
				min = i
			else:
				max = i
			#print "New minimum is",min," ;value of n is",n
			#remove the current minimum value from the list
			x.remove(min)	
			#and add it back before the nth position (the start of the remaining elements being evaluated)
			x.insert(n,min)
			#remove current maximum value from list
			x.remove(max)
			#and add it back at end of list
			x.append(max)
	return x



#import random module for random number generation
import random

#import datetime module to calculate run length
from datetime import datetime

#set the start runtime for this script
startTime = datetime.now()

#initialize list
sample = []
#populate sample list with random numbers
for i in range (0, 100):
	sample.append(random.randrange(0,10000))


print "Starting list:",sample
# print "Sorted list:",selectSort(sample)
print "Sorted list:",selectSortMinMax(sample)

#this is how long it took to run
pdq = datetime.now() - startTime
print "Processing time:", pdq
