import requests

from pages.quotes_page import QuotesPage


page_content = requests.get("http://quotes.toscrape.com/tag/life/").content
page = QuotesPage(page_content)


for quote in page.quotes:
    print(quote.content)
    print(quote.author)
    print(quote.tags)
    print("*************")
