
from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
	def walk(self):
		print("walking ...")

	@abstractmethod
	def num_legs(self):
		pass

class Dog:
	def __init__(self,name):
		self.name = name

	def num_legs(self):
		return 4

class Monkey:
	def __init__(self,name):
		self.name = name

	def num_legs(self):
		return 2


print("ABC")

d = Dog("Jesse")
print(d.num_legs())

m = Monkey("Charlie")
print(m.num_legs())

print("Iteration of these sub-classes")

animals = {Dog("Jesse"),Monkey("Charlie")}
for a in animals:
	print("%s %s has %d legs" % (a.__class__,a.name,a.num_legs()))

