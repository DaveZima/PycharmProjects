# Python 3.7
import sys
import os
import datetime
import pprint
import random
import types

#-------------------------------------------------------------------------------------#
def old_code():

    # dictionary comprehension

    friends = ["John", "Rich", "Regina"]
    last_seen = [14, 28, 96]

    # Use of a list comprehension in defining a dictionary
    new_dict = {

        # first statement defines value and second assignment
        friends[i]: last_seen[i]
        # second statement defines key loop and first assignment
        for i in range(len(friends))
        # third statement can be a conditional
        if last_seen[i] > 14
    }

    print(new_dict)

    # Combine two lists and convert to a dictionary

    friends = ["John", "Rich", "Regina"]
    last_seen = [14, 28, 96]

    new_dict = dict(zip(friends, last_seen))

    print(new_dict)

    # Lottery Coding Exercise

    # This line creates a set with 6 random numbers
    lottery_numbers = set(random.sample(range(22), 6))

    # Here are your players; find out who has the most numbers matching lottery_numbers!
    players = [
        {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
        {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
        {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
        {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
    ]

    # Then, print out a line such as "Jen won 1000.".
    # The winnings are calculated with the formula:
    # 100 ** len(numbers_matched)

    print(lottery_numbers)

    for player in players:
        print(player["name"])
        print(player["numbers"])
        print(player["numbers"].intersection(lottery_numbers))

        name = player["name"]
        hits = len(player["numbers"].intersection(lottery_numbers))
        print(f"{name} hits={hits} won {100 ** hits}")

    # print() examples
    print("print() examples")

    print("print(expr)")
    print("Hello" + " World")
    print("print(expr,expr,sep=)")
    print(22,33,sep="|")
    print("print(C style % formatting")
    print("print('%s %d' % (x,y) old format specifier")
    print("%s %d" % ("Hi",22))
    print("print('{0} {1}'.format(x,y) standard format specifier")
    print("{0} {1}".format("Hi",22))
    print("f'{var1} {var2}' f string format")
    var1 = "apple"
    var2 = 22
    print(f"{var1} and {var2}")
    print("f'{expr}' f string format")
    print(f"{22 * 11}")
    print("f'{var1.upper}' f string format function reference")
    print(f"{var1.upper()}")

    # Looping through a dictionary

    friends_ages = { "Rolf":25, "Anne":37, "Bob":22 }

    # Loop through a dictionary's keys and values
    for name, age in friends_ages.items():
        print(f"{name} {age}")

    # Loop through a dictionary's values
    for age in friends_ages.values():
        print(f"{age}")

    # Loop through a dictionary's keys
    for name in friends_ages.keys():
        print(f"{name}")

    # List comprehension
    numbers = [0,1,2,3,4]

    doubled = [ _ * 2 for _ in numbers ]
    print(f"standard list comprehension: {doubled}")

    # Conditional list comprehension
    doubled = [ _ * 2 for _ in numbers if _ > 2 ]
    print(f"conditional list comprehension: {doubled}")

    # zip() iterable merge function

    friends = [ "John", "Rich", "Regina"]
    last_seen = [24,48,96]

    zip_object = zip(friends,last_seen)

    # Convert to a dictionary

    friend_dict = dict(zip_object)

    print(f"merge list friend_dict = {friend_dict}")

    # Merge list and set

    last_seen = {24,48,96}

    zip_object = zip(friends,last_seen)

    # Convert to a dictionary

    friend_dict = dict(zip_object)

    print(f"merge list and set = {friend_dict}")

    last_seen = (24,48,96)

    zip_object = zip(friends,last_seen)

    # Convert to a dictionary

    friend_dict = dict(zip_object)

    print(f"merge list and tuple = {friend_dict}")

    # enumerate() function provides a counter that starts at 0

    friends = ["John", "Rich", "Regina"]

    for counter,friend in enumerate(friends):
        print(f"counter={counter} friend={friend}")


#-------------------------------------------------------------------------------------#
def dump(obj):
    for attr in dir(obj):
        print("obj.%s = %r" % (attr, getattr(obj, attr)))

def test():
    return 1,34

def imports():
    for name, val in globals().items():
        if isinstance(val, types.ModuleType):
            yield val.__name__

class Club:

    def __init__(self,name):
        self.name = name
        self.players = []

    def __getitem__(self,i):
        return self.players[i]

    def __repr__(self):
        return f"Club {self.name}: {self.players}"

    def __str__(self):
        return f"Club {self.name} with {len(self.players)} players"

def my_func( self, n ):
    return n * 2


##########
# main() #
##########

print("Python program %s" % (sys.argv[0]))
print("Python version %s" % (sys.version.split(" ")[0]))

my_club = Club("Bears")
my_club.players.append("Mack")
print(f"__str__ {my_club.__str__()}")
print(f"__repr__ {my_club.__repr__()}")
print(f"__getitem__ {my_club.__getitem__(0)}")

modulenames = set(sys.modules) & set(globals())
allmodules = [sys.modules[name] for name in modulenames]
print(allmodules)






