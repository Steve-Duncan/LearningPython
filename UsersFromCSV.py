#import csv module
import csv
#csv input file
fileName = "us-500.csv"

#open file for input and assign as f
with open("us-500.csv", 'rU') as f:
	#read contents of file	
	reader = csv.reader(f)
	#get the first row for headers
	headerRow = reader.next()

	#verify first row contains desired headers
	# for i in range (len(headerRow)):
	# 	print headerRow[i]

	#read each row of imported file
	for row in reader:
		#print user first and last name (first two fields in row)
		print row[0],row[1]
		#enumerate each field in row and get index and value
		for ndx,field in enumerate(row):
			#print each field in row with field from header row by matching index 
			print headerRow[ndx],":",field
		#print separator
		print "-"*14

		