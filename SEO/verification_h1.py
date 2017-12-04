from bs4 import BeautifulSoup
from urllib.request  import urlopen
import urllib.request as request

website = request.urlopen('http://wapa.pe')
soup = BeautifulSoup(website)
for h1 in soup.find_all('h1'):
    print('h1: ', h1)
