##!/usr/bin/env python

__version__ = "1.0.0"
__author__ = "Dave Zima"

###########
# Imports #
###########

# Standard library imports

import re

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

"""
Our definition of a secure filename is:
- The filename must start with an English letters or a number (a-zA-Z0-9).
- The filename can **only** contain English letters, numbers and symbols among these four: `-_()`.
- The filename must end with a proper file extension among `.jpg`, `.jpeg`, `.png` and `.gif`
"""


def is_filename_safe(filename):

	pattern = "[a-zA-Z0-9][a-zA-Z0-9_()-]*.(jpg|jpeg|png|gif)"
	results = re.match(pattern,filename)
	if results:
		return True
	else:
		return False


#--------------------------------------------------------------------------------#
def main():

	print("******************")
	print("* regex exercise *")
	print("******************\n")
	"""
	file_1.jpeg
	2file.jpg
	App)le.png
	Oran-ge.gif
	"""

	fn = "file_1.jpeg"
	if is_filename_safe(fn):
		print("%s is safe" % (fn))
	else:
		print("%s is NOT safe" % (fn))

	fn = "2file.jpg"
	if is_filename_safe(fn):
		print("%s is safe" % (fn))
	else:
		print("%s is NOT safe" % (fn))

	fn = "App)le.png"
	if is_filename_safe(fn):
		print("%s is safe" % (fn))
	else:
		print("%s is NOT safe" % (fn))

	fn = "Oran-ge.gif"
	if is_filename_safe(fn):
		print("%s is safe" % (fn))
	else:
		print("%s is NOT safe" % (fn))



	# Exit gracefully
	raise SystemExit(0)

################
# Module Start #
################

if __name__ == "__main__":
	main()
