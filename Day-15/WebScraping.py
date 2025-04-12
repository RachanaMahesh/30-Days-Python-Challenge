# Webscraping : Parsing the content from the website & pulling out the information that u exactly want
# pip install beautifulsoup4, pip install lxml
# Parser: 
# pip install lxml or pip install html5lib
# here are also differences between HTML parsers. If you give Beautiful Soup a perfectly-formed HTML document, these differences won't matter. One parser will be faster than another, but they'll all give you a data structure that looks exactly like the original HTML document.
# But if the document is not perfectly-formed, different parsers will give different results. Here's a short, invalid document parsed using lxml's HTML parser. Note that the <a> tag gets wrapped in <body> and <html> tags, and the dangling </p> tag is simply ignored:
# BeautifulSoup("<a></p>", "lxml")
# # <html><body><a></a></body></html>
# Here's the same document parsed using html5lib:
# BeautifulSoup("<a></p>", "html5lib")
# # <html><head></head><body><a><p></p></a></body></html>
# Instead of ignoring the dangling </p> tag, html5lib pairs it with an opening <p> tag. html5lib also adds an empty <head> tag; lxml didn't bother.
# Here's the same document parsed with Python's built-in HTML parser:
# BeautifulSoup("<a></p>", "html.parser")
# # <a></a>
# Like lxml, this parser ignores the closing </p> tag. Unlike html5lib or lxml, this parser makes no attempt to create a well-formed HTML document by adding <html> or <body> tags.

from bs4 import BeautifulSoup
import requests

with open("Simple.html",'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# print(soup)
# print(soup.prettify())
# print(soup.title) # which can also be written as  print(soup.find('title')
# print(soup.find('title').text) # print(soup.title.text)
# print(soup.find('div')) # retuns first div content which can also be written as print(soup.div)
# print(soup.find('div', class_ = "article")) # as class has a predefined meaning

# article = soup.find("div", class_ = "article")
# headline = article.h2.text
# print(headline)
# summary = article.p.text
# print(summary)


for article in soup.find_all("div", class_ = "article"):
    headline = article.h2.text
    print(headline)
    summary = article.p.text
    print(summary)
    print()