class MathDojo(object):
	def __init__(self,result=0):
		self.result=result

	def add(self,arg1,*rest):
		# *rest is a tuple of all arguments passed after the first arg
		# set result equal to the first argument + the sum of remaining args
	
		self.result += (arg1 + sum(rest))
		return self

	def subtract(self,arg1,*rest):
		# set result equal to the first argument - the sum of remaining args
		self.result -= (arg1 + sum(rest))
		return self

md=MathDojo()
print md.add(2).add(2, 5).subtract(3, 2).result



