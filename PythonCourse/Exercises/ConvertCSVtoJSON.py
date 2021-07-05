# Python 3.7
import sys
import os
import datetime
import ntpath
import json

#-------------------------------------------------------------------------------------#
def main():
    """
       Convential main function
    """
    print("Python program: %s" % (ntpath.basename(sys.argv[0])))
    print("Python version: %s" % (sys.version.split(" ")[0]))

    print("*************")
    print("Quiz Exercise")
    print("*************")

    # Please read the instructions carefully and write your script here:
    # You need to:
    # - read data from csv_file.txt
    # - process data and convert them into a single JSON object
    # - store the JSON object into json_file.txt
    # Your code starts here:

    # Read CSV file into a list of strings
    csv_file = open("csv_file.txt","r")
    csv_lines_raw = csv_file.readlines()
    csv_file.close()
    csv_lines = [ line.rstrip("\n") for line in csv_lines_raw ]

    """ 
    Parse the list of CSV strings and split each string into  
    fields that are added to a list of dictionaries 
    """
    json_list = []
    for csv_line in csv_lines:
        col_list = csv_line.split(",")
        club = col_list[0]
        city = col_list[1]
        country = col_list[2]
        d = {"club":club,"country":country,"city":city}
        json_list.append(d)

    json_file = open("json_file.txt","w")
    json.dump(json_list,json_file)
    json_file.close()

    raise SystemExit(0)

################
# Module Start #
################

__version__ = "1.0.0"

if __name__ == "__main__":
    main()






