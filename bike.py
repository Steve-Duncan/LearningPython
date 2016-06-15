#create class of Bike
class Bike(object):
	def __init__(self, price,max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 10
		self.name = self
		


	def displayInfo(self):
		print "price: $" + str(self.price)
		print "maximum speed: " + str(self.max_speed) + "mph"

		print "total miles ridden:", self.miles
		return self

	def ride(self,num):
		self.num = num
		print "Riding",num,"times"
		#print "Total miles ridden: " + str(self.miles+10)
		self.miles += 10 * num
		return self

	def reverse(self,num):
		self.num = num
		print "Reversing",num,"times"
		self.miles -=5 * num
		return self



#create 3 instances of Bike and pass values for price and max speed
bike1 = Bike(150,20)
bike2 = Bike(250,30)
bike3 = Bike(175,25)


print "\nbike1:"
#call ride function 3 times, reverse function 3 times and display info
bike1.ride(3).reverse(4).displayInfo()

print "\nbike2:"
# #call ride function 2 times, reverse function 2 times and display info
bike2.ride(2).reverse(2).displayInfo()

print "\nbike3:"
# #call reverse function 3 times and display info
bike3.reverse(3).displayInfo()

# #to prevent having negative miles,I would change the reverse method to not subtract miles;
# #since miles ridden in opposition are still miles ridden. So the calculation would be for 
# #the absolute value of miles ridden


