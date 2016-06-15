class Animal(object):
	def __init__(self,name):
		self.name=name
		self.health=100

	def walk(self,num):
		self.health -= 1 * num
		return self

	def run(self,num):
		self.health -=5 * num
		return self


	def displayHealth(self):
		print self.name,"Health:",self.health
		return self


class Dog(Animal):
	def __init__(self,name):
		super(Animal,self).__init__()
		self.health=150
		self.name = name

	def pet(self,num):
		self.health += 5 * num
		return self

class Dragon(Animal):
	def __init__(self,name):
		super(Animal,self).__init__()

		self.name = name
		self.health = 170

	def fly(self,num):
		self.health -=10 * num
		return self



animal = Animal("animal")
animal.walk(3).run(2).displayHealth()

dog1 = Dog("puppy")
dog1.walk(3).run(1).pet(1).displayHealth()

dragon = Dragon("Yurassis")
dragon.walk(3).run(2).fly(2).displayHealth()

#verify methods in subclasses don't apply to other subclasses, but methods inherited
#from parent class do apply
#animal.pet(1)
#animal.fly(1)



