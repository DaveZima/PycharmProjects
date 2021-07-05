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

# Third-party library imports

# Application library imports

from bs4 import BeautifulSoup
import re
import requests


####################
# Global Variables #
####################
HTML="""
<!DOCTYPE html>
<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">lorem ipsum dolar sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>
"""

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock
</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>
</body></html>
'''

###########
# Classes #
###########
class ParsedItem:
	"""
	A class to take in an HTML page or content, and find properties of an item
	in it.
	"""
	def __init__(self, page):
		self.soup = BeautifulSoup(page, 'html.parser')

	def name(self):
		locator = 'article.product_pod h3 a'
		item_name = self.soup.select_one(locator).attrs['title']
		return item_name

	def link(self):
		locator = 'article.product_pod h3 a'
		item_url = self.soup.select_one(locator).attrs['href']
		return item_url

	def price(self):
		locator = 'article.product_pod p.price_color'
		item_price = self.soup.select_one(locator).string

		pattern = '£([0-9]+\.[0-9]+)'
		matcher = re.search(pattern, item_price)
		return float(matcher.group(1))

	def rating(self):
		locator = 'article.product_pod p.star-rating'
		star_rating_element = self.soup.select_one(locator)
		classes = star_rating_element.attrs['class']
		rating_classes = filter(lambda x: x != 'star-rating', classes)
		return next(rating_classes)


#############
# Functions #
#############

#--------------------------------------------------------------------------------#
def main():

	print("***************")
	print("* simple_html *")
	print("***************\n")

	html_parser = BeautifulSoup(HTML,"html.parser")

	print(html_parser.find("h1"))
	print(html_parser.find("h1").string)

	print("multiple tag test - what happens when there are multiples")
	print(html_parser.findAll("p"))

	l = html_parser.findAll("li")
	fl = [ x.string for x in l]
	print(fl)

	print("*************")
	print("* Item HTML *")
	print("*************\n")

	html_parser = BeautifulSoup(ITEM_HTML,"html.parser")

	print("\nFind the Title of first book using a CSS hierarchy locator\n")

	# Define the search tag hierarchy in the HTML
	# article tag with class product_pod
	locator = "article.product_pod h3 a" # CSS locator
	item_link = html_parser.select_one(locator) # Only one instance of the CSS locator
	# Should return html_parser = BeautifulSoup(HTML,"html.parser")
	print(item_link)
	# <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
	item_name = item_link.attrs["title"]
	print(item_name)

	print("\nFind the Price of first book using a CSS hierarchy locator\n")

	# <p class="price_color">£51.77</p>
	locator = "article.product_pod p.price_color" # CSS locator
	item_link = html_parser.select_one(locator) # Only one instance of the CSS locator
	item_price_str = item_link.string
	print(item_price_str)
	n = re.search("[0-9]+\.[0-9]+",item_price_str)
	print("n = %s" % (n.string))

	item = ParsedItem(ITEM_HTML)
	print("Class %f" % (item.price()))


	# Exit gracefully
	raise SystemExit(0)

################
# Module Start #
################

if __name__ == "__main__":
	main()
