##!/usr/bin/env python
"""
Script/Module:  importing_modules_exercise.py

Parameters:     N/A

Description:    Import modules and build a Calculator class.

Revision History:

Version  Date       Author              Description
-------- ---------- ------------------- -------------------------------------------------------------
1.0.0    2021-04-03 Dave Zima           It lives
"""
__version__ = "1.0.0"
__author__ = "Dave Zima"

###########
# Imports #
###########

# Standard library imports

# Third-party library imports

# Application library imports
from addition import Addition
from addition import Calculator

####################
# Global Variables #
####################

###########
# Classes #
###########

#############
# Functions #
#############

#-------------------------------------------------------------------------------------------#
def main():

	x = Calculator.add(3,1)
	print(f"add(3,1) = {x}")

	x = Calculator.subtract(5,1)
	print(f"subtract(5,2) = {x}")

	x = Calculator.multiply(1,8)
	print(f"multiply(1,8) = {x}")

	x = Calculator.divide(8,2)
	print(f"divide(8,2) = {x}")

	x = Calculator.divide(8,3)
	print(f"divide(8,3) = {x}")

	raise SystemExit(0)

################
# Module Start #
################

""" 
The starting executing script/module __name__ will always be __main__ 
and the standard coding convention is to execute a main function.
"""
if __name__ == "__main__":
	main()
