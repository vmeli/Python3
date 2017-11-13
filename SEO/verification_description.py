import urllib.request as request
from bs4 import BeautifulSoup

web_site = request.urlopen('http://wapa.pe/trending/1144709-esta-es-la-arana-mas-adorable-del-mundo-y-acabara-con-tu-aracnofobia-video')
soup = BeautifulSoup(web_site)
description = soup.find('meta', attrs={'name': "description"})
length_description = len(description.get('content'))
print('Tamaño de la descripción: ', length_description)
if (length_description < 154):
    print('La descripción no supera los 154 caracteres')
