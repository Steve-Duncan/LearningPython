######################################################################
# #crawler, part 1
#Crawl the coding dojo site and extract all links. Create list of all
#unique href locations.
######################################################################

# import the urlopen function from the urllib2 module
from urllib2 import urlopen
# import the BeautifulSoup function from the bs4 module
from bs4 import BeautifulSoup
# import pprint to print things out in a pretty way
import pprint
# choose the url to crawl
url = 'http://www.codingdojo.com'
# get the result back with the BeautifulSoup crawler
soup = BeautifulSoup(urlopen(url))
#print soup # print soup to see the result!!
# your code here to find all the links from the result
# and complete the challenges below
######################################################################

def UniqueList(links):

	#initialize a list to contain unique values
	uniqueList = []
	#iterate the list of links
	for link in links:
		line = link['href']
		#filter out junk we don't want in the list
		if ("#" in line) or ("javascript:void" in line):
			pass
		else:
			#check if value is already in the list
			if not line in uniqueList:
				#add value to unique list
				uniqueList.append(str(line))


	#use the pprint function to output the list items as desired
	pprint.pprint(uniqueList)


######################################################################
# #crawler, part 2
# Modify code from part 1: create dictionary with links as keys. Since
# dictionary keys are unique, set the value to the number of times the
# link is found.
######################################################################

def CreateDict(links):

	#create empty dictionary
	linkDict = {}
	#initialize counter
	count = 1
	#iterate through all links
	for link in links:
		#find links that contain href and convert to string from unicode
	 	line = str(link['href'])
	 	#filter out junk we don't want in the list
	 	if not ("javascript:void" in line) and not ("#" in line):
	 		#check if value is already in the dictionary
	  	  	if not line in linkDict:
	  	  		#reset counter
	 		 	count = 1
	 		 	#add line to dictionary
	 		 	linkDict[line] = count
	 		else:
	 		 	#get count value for item and increment counter
	 	 	 	count = linkDict[line] + 1
	 	 	 	#update count value for line
	 	 	 	linkDict[line] = count
		 		

	#print the dictionary
	pprint.pprint(linkDict)

#grab all a tags that contain an href value
links = soup.find_all('a', href=True)

#call function to create list of unique values
print "######################################################################"
print "#"
print "#crawler, part 1"
print "#"
print "######################################################################"
UniqueList(links)

#call function to create dictionary with count of link instances
print "######################################################################"
print "#"
print "#crawler, part 2"
print "#"
print "######################################################################"
CreateDict(links)