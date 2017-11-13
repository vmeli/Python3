import urllib.request as request 

request_path = request.Request('http://wapa.pe/')
answer = request.urlopen(request_path)
print('HTTP OR HTTPS: ', answer.geturl())
