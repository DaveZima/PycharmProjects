##!/usr/bin/env python
"""
Script/Module:  app.py

Parameters:     N/A

Description:    Python script used in the Milestone 2 Database project

Revision History:

Version  Date       Author              Description
-------- ---------- ------------------- -------------------------------------------------------------
1.0.0    2021-04-04 Dave Zima           It lives
"""
__version__ = "1.0.0"
__author__ = "Dave Zima"

###########
# Imports #
###########

# Standard library imports

import sys

import json

# Third-party library imports

# Application library imports

from utils import database

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
def main():

	# Get the database list data
	books = database.load_database_list()

	# Print the screen title
	print("***********************************")
	print("* Milestone 2 Project - Databases *")
	print("***********************************")

	# Build main menu list
	main_menu = [
	"Add a new book",
	"List all books",
	"Mark a book to read",
	"Delete a book",
	"Quit" ]

	while True:
		# list_menu() ensures that one of the choices has been selected
		choice = database.list_menu(main_menu,"Main Menu")
		if choice == 1:
			database.add_book(books)
		elif choice == 2:
			database.list_books(books)
		elif choice == 3:
			database.mark_book(books)
		elif choice == 4:
			books = database.delete_book(books)
		else:
			break

	# Exit gracefully

	database.save_database_list(books)

	# database.create_book_table()

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
