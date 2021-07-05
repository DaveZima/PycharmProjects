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

import requests

# Third-party library imports

from HTML.pages.quotes_page import QuotesPage

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
def main():

	print("app.py")

	page_content = requests.get('http://quotes.toscrape.com').content

	print(page_content)

	raise SystemExit(0)

	page = QuotesPage(page_content)

	for quote in page.quotes:
		print(quote.content)

	# Exit gracefully
	raise SystemExit(0)

################
# Module Start #
################

if __name__ == "__main__":
	main()
