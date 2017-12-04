from urllib.request  import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://wapa.pe')
#html = urlopen('https://rosatel.pe/lima/')
#html = urlopen('https://elcomercio.pe/')
soup = BeautifulSoup(html.read())
print("Texto del title: ", soup.html.head.title.string)
print("Tamaño title : ", len(soup.html.head.title.string))
