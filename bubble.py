
#I don't understand the pseudo code in the platform so I used what made sense to me.

#set variable = some value(s)
#get length of list -1; this is how many passes are required to complete sort
#for each pass through list
#	for each value in list
# 	get first value from list
# 	get second value from list
# 	if first value > second value
# 		swap values
#repeat until all passes complete

def bubblesort(x):
#get the length of the list; it will need to run n-1 times
	for n in range (0, len(x)-1):
		#compare value with next value
	 	for i in range (0,n):
	 		#and swap values if needed
	  		if x[i] > x[i+1]:
	  			x[i],x[i+1]=x[i+1],x[i]
	return x


#much simpler to just use sort method. Nobody uses bubble sort anyway...
#x.sort()



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

#call bubblesort function and pass sample list, then output the ordered list
print bubblesort(sample)

#this is how long it took to run
pdq = datetime.now() - startTime
print "Processing time:", pdq
