from bs4 import BeautifulSoup
from urllib.request  import urlopen
import urllib.request as request
import re

website = request.urlopen('http://wapa.pe')
soup = BeautifulSoup(website)
keywords = soup.find('meta', attrs = {'name':'keywords'})
print("Keywords del website: ", keywords.get('content').lower())
words = keywords.get('content').lower().split(',')
print(words)
for word in words:
    print(word.strip(), len(soup.findAll(text=re.compile(word.strip()))))
