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

	def ride(self):
		print "Riding"
		#print "Total miles ridden: " + str(self.miles+10)
		self.miles += 10

	def reverse(self):
		print "Reversing"
		self.miles -=5



#create 3 instances of Bike and pass values for price and max speed
bike1 = Bike(150,20)
bike2 = Bike(250,30)
bike3 = Bike(175,25)


print "\nbike1:"
#call ride function 3 times
for i in range(3): bike1.ride()
#call reverse function 3 times
for i in range(3): bike1.reverse()
print "\nbike1 info:"
#call function to display info
bike1.displayInfo()

print "bike2:"
#call ride function 2 times
for i in range(2): bike2.ride()
#call reverse function 2 times
for i in range(2): bike2.reverse()
print "\nbike2 info:"
#call function to display info
bike2.displayInfo()

print "\nbike3:"
#call reverse function 3 times
for i in range(3): bike3.reverse()
print "\nbike3 info:"
#call function to display info
bike3.displayInfo()
#to prevent having negativbe miles,I would change the reverse method to not subtract miles;
#since miles ridden in opposition are still miles ridden. So the calculation would be for 
#the absolute value of miles ridden


