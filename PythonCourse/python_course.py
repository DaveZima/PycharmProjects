# Python 3.7
import sys
import os
import datetime
import ntpath

#-------------------------------------------------------------------------------------#
def main():
   """
      Convential main function
   """
   print("Python program: %s" % (ntpath.basename(sys.argv[0])))

   print("Python version: %s" % (sys.version.split(" ")[0]))

#-------------------------------------------------------------------------------------#
"""
   Convential main function call
"""
if __name__ == "__main__":
    main()






