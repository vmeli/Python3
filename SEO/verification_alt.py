from bs4 import BeautifulSoup
from urllib.request  import urlopen
import urllib.request as request

website = request.urlopen('http://wapa.pe')
soup = BeautifulSoup(website)
count = 1
print(soup.findAll('img'))
for image in soup.findAll('img'):
    #print('Image #', count, ':', image['src'])
    print('Alt de imagen #', count, ':', image.get('alt', "None"))
    count += 1
