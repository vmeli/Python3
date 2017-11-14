#coding: utf-8
from urllib.request  import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://wapa.pe')
#html = urlopen('https://elcomercio.pe/')
soup = BeautifulSoup(html.read())
print("Tamaño title : ", soup.html)
#print("Contenido title: ", soup.html.head.title.string)