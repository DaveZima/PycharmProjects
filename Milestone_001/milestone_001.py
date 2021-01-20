"""
Date:           12/31/2020
Course:         The Complete Python Course Udemy Jose Salvatierra
Project:        Milestone 1

Requirements:   1. Menu that lists functions and exits the program when the user enters Q
                2. Movie data includes title, director and release year
                3. Add new movie function
                4. List all movies function
                5. Search movie database by title
"""

import sys

##########
# Global #
##########

PROGRAM = "milestone_001.py"

movies = [
    {"Title": "The Godfather", "Director": "Frances Ford Copolla", "Release": 1972},
    {"Title": "2001 A Space Odyssey", "Director": "Stanley Kubrick", "Release": 1968},
    {"Title": "Raiders of the Lost Ark", "Director": "Steven Spielberg", "Release": 1981},
    {"Title": "Singin' in the Rain", "Director": "Stanley Donen", "Release": 1952},
    {"Title": "Star Wars: Episode IV – A New Hope", "Director": "George Lucas", "Release": 1977}
]

#############
# Functions #
#############

#--------------------------------------------------------#
def print_movie_title():

    print("%-36.36s %-24.24s %-7.7s" % ("Title", "Director", "Release"))
    print("%s %s %s" % ("-" * 36, "-" * 24, "-" * 7))

#--------------------------------------------------------#
def print_movie_line(title,director,release):

    print("%-36.36s %-24.24s %-7.7s" % (title, director, release))

#--------------------------------------------------------#
def add_movie():

    print("\n***************")
    print("* Add a movie *")
    print("***************\n")

    title = str(input("Enter the title: "))
    director = str(input("Enter the director: "))
    release = int(input("Enter the release year: "))

    d = {"Title": title, "Director": director, "Release": release}
    movies.append(d)

    print("\nNew movie added\n")

#--------------------------------------------------------#
def list_movies():

    print("\n*******************")
    print("* List all movies *")
    print("*******************\n")

    print_movie_title()

    for movie in movies:
        print_movie_line(movie["Title"],movie["Director"], movie["Release"])

    print()

#--------------------------------------------------------#
def search_movies():

    print("\n**********************")
    print("* Search for a movie *")
    print("**********************\n")

    title = str(input("Enter movie title: ")).strip()
    search_title = title.lower()

    for movie in movies:
        if movie["Title"].lower() == search_title:
            print_movie_title()
            print_movie_line(movie["Title"],movie["Director"], movie["Release"])
            print()
            break
    else:
        print(f"\nSorry the movie '{title}' was not found in the movie database\n")

########
# Main #
########

print(f"Starting {PROGRAM}")

# Display and process main menu

user_choice = None

while user_choice != "Q":

    # Display the menu
    print("***************************")
    print("*   Movie Database Menu   *")
    print("***************************")
    print("(Enter one of the following letters)\n")
    print("A - Add a new movie")
    print("L - List all movies")
    print("S - Search for a movie by Title")
    print("Q - Quit the program\n")

    # Receive choice input from the user
    user_choice = str(input("Enter your choice: ")).upper().strip()

    # Process the user's choices
    if user_choice == "A":
        add_movie()
    elif user_choice == "L":
        list_movies()
    elif user_choice == "S":
        search_movies()
    elif user_choice != "Q":
        print(f"\n'{user_choice}' is invalid. You must enter one of the following letters (A,L,S,Q)\n")

print(f"\n{PROGRAM} has completed successfully")

