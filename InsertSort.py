#insertion sort

def InsertSort(x):
	print "Start:",x
	print
	#iterate the list
	for i in range (1,len(x)):
		#set current number
		num = x[i]
		#iterate the list from current number to the left
		for j in range (i-1,-1,-1):
			#check if current number is less than number to its left
			if num < x[j]:
				#swap values for current number and smaller number, making new current number
			 	x[j+1] = x[j]
			 	x[j] = num 
			else:
				#get next current number to check
			 	num = x[j+2]
			 	break
		#print x	#this shows successive values of list for each iteration

	print "Sorted:",x


# #sample list
# x = [6,5,3,1,8,7,2,4]

# #call function to sort list with Insertion Sort
# InsertSort(x)


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

#call function to sort list with Insertion Sort
InsertSort(sample)

#this is how long it took to run
pdq = datetime.now() - startTime
print "Processing time:", pdq