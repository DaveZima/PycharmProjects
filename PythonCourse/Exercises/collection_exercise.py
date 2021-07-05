##!/usr/bin/env python
"""
Script/Module:  template.py

Parameters:     N/A

Description:    This is a python template or shell to be used when starting a new module/script.
                The code template helps to give modules a standard look and structure.

Revision History:

Version  Date       Author              Description
-------- ---------- ------------------- -------------------------------------------------------------
1.0.0    2021-03-31 Dave Zima           It lives
"""
__version__ = "1.0.0"
__author__ = "Dave Zima"

###########
# Imports #
###########

# Standard library imports

from collections import defaultdict, OrderedDict, namedtuple, deque

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



def task1() -> defaultdict:
	"""
	- create a `defaultdict` object, and its default value would be set to the string `Unknown`.
	- Add an entry with key name `Alan` and its value being `Manchester`.
	- Return the `defaultdict` object you created.
	"""
	# you code starts here:
	coworkers = [("Alan","Manchester")]
	ala_maters = defaultdict(list)
	for coworker, school in coworkers:
		ala_maters[coworker].append(school)
	return ala_maters


def task2(arg_od: OrderedDict):
	"""
	- takes in an OrderedDict `arg_od`
	- Remove the first and last entry in `arg_od`.
	- Move the entry with key name `Bob` to the end of `arg_od`.
	- Move the entry with key name `Dan` to the start of `arg_od`.
	- You may assume that `arg_od` would always contain the keys `Bob` and `Dan`,
		and they won't be the first or last entry initially.
	"""
	# you code starts here:
	pass


def task3(name: str, club: str) -> namedtuple:
	"""
	- create a `namedtuple` with type `Player`, and it will have two fields, `name` and `club`.
	- create a `Player` `namedtuple` instance that has the `name` and `club` field set by the given arguments.
	- return the `Player` `namedtuple` instance you created.
	"""
	# you code starts here:
	pass


def task4(arg_deque: deque):
	"""
	- Manipulate the `arg_deque` in any order you preferred to achieve the following effect:
		-- remove last element in `deque`
		-- move the fist (left most) element to the end (right most)
		-- add an element `Zack`, a string, to the start (left)
	"""
	# you code starts here:
	pass

#--------------------------------------------------------------------------------#
def main():

	print("************************")
	print("* Collections Exercise *")
	print("************************\n")

	l = task1()

	# Exit gracefully
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
