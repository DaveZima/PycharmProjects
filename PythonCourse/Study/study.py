
###########
# Imports #
###########

# Standard library imports
import sys
# Third-party library imports

# Application library imports

#############
# Functions #
#############

def builtin_datatypes():

	print("Built-in Data Types\n")
	print("Number Types")
	print("------------\n")
	i = 1234567890123456789012345678901234567890
	i += 1
	print("Integer: Unlimited precision 40 digit test = %d" % (i))
	print("Float: 15 digits 10-307 to 10+308")
	print("Complex: real number + imaginary number. Imaginary numbers are negative when squared")
	print("")
	print("Sequence Types")
	print("--------------\n")
	print("list (mutable) []")
	print("tuple (immutable) (a,b,c) or a,b,c # comma makes the tuple")
	print("range (immutable) range(start,stop,step) produces a list of integers")
	print("string (imutable) sequence of unicode code points")
	print("byte (immutable) b = bytes('abc') sequence of single bytes")
	print("bytearray (immutable) ba = bytearray('abc') ")
	print("")
	print("Set Types")
	print("---------\n")
	print("set (mutable) {} - an unordered collection of distinct hashable objects.")
	print("frozenset (immutable) {} - an unordered collection of distinct hashable objects used by dict key")
	print("")
	print("Mapping Types")
	print("-------------\n")
	print("dict(mutable) set of key/value pairs")

def comprehensions():

	l = [1,2,3]
	s = {1,2,3}
	t = 1,2,3
	d = [{"diet_rating": 1},{"diet_rating": 2}]

	print("Comprehensions are single line statements in which you can parse and transform iterables with a condition")
	print("Python implements these because many iterable transformations are simple and common")
	print("")

	l2 = [n * 2 for n in l]
	print("list comprehension - parsing and transforming a list is a single statement")
	print("l2 = [n * 2 for n in l]")
	print(l2)
	print("")

	print("dictionary comprehension with condition")
	d2 = [ i["diet_rating"] * 2 for i in d if i["diet_rating"] == 1]
	print('d2 = [ i["diet_rating"] * 2 for i in d if i["diet_rating"] == 1]')
	print(d2)
	print("")

	print("set comprehension")
	s2 = [ n * 10 for n in s ]
	print("s2 = [ n * 10 for n in s ]")
	print(s2)
	print("")

def zip_demo():

	print("The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together")
	print("")
	friends = ["John","Paul","Jones"]
	ages = [34,39,102]
	z = zip(friends,ages)
	d = dict(z)
	print("Combine two lists into a dictionary d = dict(z)")
	print(d)

def lambda_demo():

	print("A lambda function is an anonymous function that can take any number of arguments, but can only have one expression.")
	print("divide = lambda x,y: x/y")
	print("Yet another single statement simple shorthand that can done on the fly")
	divide = lambda x,y: x/y
	x = divide(10,5)
	print("x = divide(10/5) where x = %d" % (x))

def error_trapping():

	print("Error Trapping - except:  except error: else: (exeption not trapped) finally: (always run)")


########
# main #
########

# builtin_datatypes()
# comprehensions()
# zip_demo()
# lambda_demo()
error_trapping()