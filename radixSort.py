
def RadixSort(listToSort,verbose):
	# get array to sort

	print "Unsorted:",listToSort

	#get max value of list, convert to string and count digits
	#this tells us how many passes to make
	passes = len(str(max(listToSort)))
	if verbose: print "The max value in list to be sorted is",max(listToSort),"which contains",passes,"digits, so will require",passes,"passes to sort"
	#for each sorting pass
	for i in range(0,passes):
		#set the divisor for calculating the digit's place; i determines the number of 0s to be used.
	 	div = '1'+i*'0'
	 	if verbose: print "Sorting list by values in",str(div)+"'s place"
	 	#create empty list to hold values while being sorted
		sortBucket = [[] for s in range(10)]

	 	#get each element from listToSort
	 	for element in (listToSort):
	 		#calculate the digit we need, based on place value (1s, 10s, 100s, etc)
	 		digit = (element / int(div)) % 10

	 		#uncomment this print statement to show which elements are being added to which lists
	 		if (verbose): print "\tadd",element,"to",digit,"list in sort bucket list"

	 		#add the element from list to sort to the appropriate holding bucket in sort bucket list
	 		sortBucket[digit].append(element)
	 	#clear the list to sort

	 	listToSort[:] = []
	 	#and copy semi-sorted values into list from bucket list
	 	#enumerate bucket list
		for ndx,l in enumerate(sortBucket):
			#enumerate nested lists
			for ndx,n in enumerate(l):
				#add element to list to sort
				listToSort.append(n)
		#print semi-sorted list for each pass
	 	if i+1 == passes:
	 		print "Sorted:",listToSort
	 	else:
	 		if verbose:
	 			print "This is the list to be sorted after pass#",i+1
				print listToSort

########################################################################
listToSort = [101, 843, 91, 230,2598]
#to print comments during sort, call function with value of True
RadixSort(listToSort,False)


