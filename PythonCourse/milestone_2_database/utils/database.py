###########
# Imports #
###########

# Standard library imports

# Third-party library imports

# Application library imports
import json
import sqlite3

#############
# Functions #
#############

#--------------------------------------------------------------------------------#
def create_book_table():

	db_con = sqlite3.connect("data.db")
	db_cur = db_con.cursor()

	db_cur.execute("create table books(name text primary key,author text,read integer)")

	db_con.commit()
	db_con.close()

#--------------------------------------------------------------------------------#
def db_add_book():

	db_con = sqlite3.connect("data.db")
	db_cur = db_con.cursor()

	db_con.commit()
	db_con.close()

#--------------------------------------------------------------------------------#
def list_menu(list,title):

	if len(list) == 0:
		return 0
	else:
		total_choices = len(list)

	# Create a multi-line menu string
	menu_str = ""
	menu_str += "\n%s\n" % (title)
	menu_str += "-" * len(title) + "\n"
	for count, item in enumerate(list):
		menu_str += "[%s] %s\n" % (count+1,item)

	while True:

		print(menu_str)
		choice = input("Enter a choice: ")
		try:
			choice_int = int(choice.strip())
		except:
			choice_int = -1

		if ( choice_int > 0 and choice_int <= total_choices ):
			break
		else:
			if choice_int == -1:
				x = input("\nInvalid non-numeric choice '%s'. \n(Press any key to try again) " % (choice))
			else:
				x = input("\nInvalid choice '%d'. \n(Press any key to try again) " % (choice_int))

	# while True:

	return choice_int

#--------------------------------------------------------------------------------#
def mark_book(books):

	menu = [ d["name"] for d in books ]
	no_of_choices = len(menu)
	menu.append("CANCEL")

	choice = list_menu(menu,"Select a Book")

	# list_menu() guarantees that a valid choice was made and
	# no_of_choices + 1 = CANCEL
	if choice != ( no_of_choices + 1 ):
		book_index = choice - 1
		books[book_index]["read"] = True

#--------------------------------------------------------------------------------#
def delete_book(books):

	menu = [ d["name"] for d in books ]
	no_of_choices = len(menu)
	menu.append("CANCEL")

	choice = list_menu(menu,"Select a Book")

	# list_menu() guarantees that a valid choice was made and
	# no_of_choices + 1 = CANCEL
	if choice != ( no_of_choices + 1 ):
		book_index = choice - 1
		book_name = books[book_index]["name"]
		books = [ d for d in books if d["name"] != book_name ]
	# print("--------------")
	# print("After delete")
	# print("--------------")
	# print(books)

	return books

#--------------------------------------------------------------------------------#
def add_book(books):

	print("**************")
	print("* Add a book *")
	print("**************")

	book_name = input("Book Name: ")
	book_author = input("Book Author: ")
	book_read = False
	books.append({"name":book_name,"author":book_author,"read":book_read})

#--------------------------------------------------------------------------------#
def list_books(books):

	if len(books) == 0:
		print("\nThere are no books in the database")
	else:
		title = "*** Book Database ***".center(70," ")
		print("%s\n" % (title))
		print("%-32.32s %-24.24s %-10.10s" % ("Book Name","Book Author","Read?"))
		print("-" * 32 + " " + "-" * 24 + " " + "-" * 10)
		for book in books:
			name = book["name"]
			author = book["author"]
			read = book["read"]
			print("%-32.32s %-24.24s %-10.10s" % (name,author,read))

	x = input("\nPress any key to continue ")

#--------------------------------------------------------------------------------#
def save_database_list(books):

	with open('database_list.json', 'w') as fout:
		json.dump(books, fout)

#--------------------------------------------------------------------------------#
def load_database_list():

	global books

	with open('database_list.json', 'r') as fin:
		books = json.load(fin)

	return books

##########
# Module #
##########

# if __name__ == "utils.database":
# 	print("Hey - database module starting !!!!!!!!!!!!")
