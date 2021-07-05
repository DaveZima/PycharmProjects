from bs4 import BeautifulSoup
from HTML.locators.quote_page_locators import QuotesPageLocators
from HTML.parsers.quote import QuoteParser



###########
# Classes #
###########

#--------------------------------------------------------------------------------#
class QuotesPage:
	def __init__(self,page):
		self.soup = BeautifulSoup(page,"html.parser")

	@property
	def quotes(self):
		return [QuoteParser(e) for e in self.soup.select(QuotesPageLocators.QUOTE)]

print("MODULE: pages.quotes_page.py")
