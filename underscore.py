
class Underscore(object):
	def map(self,arr,func):
		newList = []										#initialize new list
		for val in arr:										#iterate elements in passed list
			newList.append(func(val))						#apply passed function to elements and append to new list
		return newList


	def reduce(self,arr,func):
		val = arr[0]										#get the value of first element of passed array
	 	for ndx in range(1,len(arr)):						#iterate passed list
	 		val = func(val,arr[ndx])						#pass current value of val and array element to passed function
	 	return val


	def find(self,arr,func):								
		for val in arr:										#iterate passed list
			if func(val):									#return the first instance that meeds condition in passed function
				return [val]			


	def filter(self,arr,func):
		newList=[]											#initialize new list
		for val in arr:										
			newList.append(val) if func(val) else None		#append to new list each element that meets condition in passed function
		return newList


	def reject(self,arr,func):
		newList=[]											#initialize new list
		for val in arr:										
			newList.append(val) if not func(val) else None		#append to new list each element that fails condition in passed function
		return newList


_ = Underscore() # instantiate Underscore class

myList = [1,2,3,4,5]

#call methods of Underscore class, passing in list and function; print returned list
#the passed function can be lambda or a previously defined named function

print _.map(myList,lambda x: x+5)

print _.reduce(myList,lambda x,y: x*y)

print _.find(myList,lambda x: x==4)

print _.filter(myList,lambda x: x>=3)

print _.reject(myList,lambda x: x>=3)



