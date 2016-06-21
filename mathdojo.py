class MathDojo(object):
	def __init__(self,result=0):
		self.result=result

	def add(self,arg1,*rest):
		# *rest is a tuple of all arguments passed after the first arg
		
		tmpList = list(rest)								#convert args in tuple to list
		tmpList.insert(0,arg1)								#add arg(s) not in tuple to list
		for t in range (0,len(tmpList)):					#iterate elements in list
			if type(tmpList[t]) is list:					#if element is list:
				self.result += (sum(tuple(tmpList[t])))		#convert list to tuple and sum elements of tuple				
			elif type(tmpList[t]) is tuple:					#if element is tuple:
				self.result += sum(tmpList[t])				#sum elements of the tuple
			else:											#if singleton:
				self.result += tmpList[t]					#add element to total
		return self

	def subtract(self,arg1,*rest):
		tmpList = list(rest)								#convert args in tuple to list
		tmpList.insert(0,arg1)								#add arg(s) not in tuple to list
		for t in range (0,len(tmpList)):					#iterate elements in list
			if type(tmpList[t]) is list:					#if element is list:
				self.result -= (sum(tuple(tmpList[t])))		#convert list to tuple and subtract sum of elements in tuple
			elif type(tmpList[t]) is tuple:					#if element is tuple:
				self.result -= sum(tmpList[t])				#subtract the sume of elements in the tuple				
			else:											#if singleton:
				self.result -= tmpList[t]					#subtract element from total
		return self

md=MathDojo()												#instantiate MathDojo class

print md.add([1],3,4).add((3,6,9),[3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3],(.15,)).result




