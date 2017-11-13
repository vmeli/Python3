import urllib.request as request 

request_path = request.Request('http://wapa.pe/')
answer = request.urlopen(request_path)
print('HTTP OR HTTPS: ', answer.geturl())

url = 'http://wapa.pe/'
print('url: ', url)
site = request.urlopen(url)
meta = site.info()
print('Content-Encoding: ', site.headers['content-encoding'],dir(site.headers))
