##!/usr/bin/env python
"""
Script/Module:  template.py

Parameters:     N/A

Description:    Turn a prime number function into a prime number generator

Revision History:

Version  Date       Author              Description
-------- ---------- ------------------- -------------------------------------------------------------
1.0.0    2021-05-22 Dave Zima           It lives
"""
__version__ = "1.0.0"
__author__ = "Dave Zima"

###########
# Imports #
###########

# Standard library imports

# Third-party library imports

# Application library imports

####################
# Global Variables #
####################

###########
# Classes #
###########

#############
# Functions #
#############

#--------------------------------------------------------------------------------#
def orig_prime_number():

	for n in range(2,20):
		prime = True
		for x in range(2,n):
			if n % x == 0:
				prime = False
				break
		if prime:
			print("prime number %d" % (n))

#--------------------------------------------------------------------------------#
def prime_numbers():

	for n in range(2,100):
		prime = True
		for x in range(2,n):
			if n % x == 0: # divisor
				prime = False
				break
		if prime:
			yield n

# Define a PrimeGenerator class
#--------------------------------------------------------------------------------#
class PrimeGenerator:
	# You may modify the __init__() method if necessary, but you don't need to change its arguments
	def __init__(self, stop):
		self.stop = stop    # stop defines the range (exclusive upper bound) in which we search for the primes
		self.number = 2

	def __next__(self):
		print("range(%d,%d)" % (self.number,self.stop))
		for n in range(self.number,self.stop):

			prime = True
			# loop through all previous integers
			print("testing n = %d" % (n))
			print("sub range(%d,%d)" % (2,n))
			for x in range(2,n):
				# if you can divide a previous integer evenly (no remainder) then n is not prime
				if n % x == 0:
					prime = False
					break
			if prime:
				self.number = n + 1
				return n
			else:
				return StopIteration()

#--------------------------------------------------------------------------------#
def main():

	print("Prime Number Generator\n")

	prime_gen = PrimeGenerator(100)
	print("First prime = %d" % (prime_gen.number))
	print("--------------------------------------")
	next(prime_gen)
	print("Next prime = %d" % (prime_gen.number))
	print("--------------------------------------")
	next(prime_gen)
	print("Next prime = %d" % (prime_gen.number))
	print("--------------------------------------")
	next(prime_gen)
	print("Next prime = %d" % (prime_gen.number))
	print("--------------------------------------")
	next(prime_gen)
	print("Next prime = %d" % (prime_gen.number))
	print("--------------------------------------")

	# Exit gracefully
	raise SystemExit(0)

################
# Module Start #
################

if __name__ == "__main__":
	main()
