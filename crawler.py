#crawler, part 1.

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

#grab all a tags that contain an href value
links = soup.find_all('a', href=True)
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
