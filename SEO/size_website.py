#coding: utf-8
import urllib.request as request
import os

url = 'http://www.python.org/'
print('url: ', url)
site = request.urlopen(url)
meta = site.info()
print('Content-Length: ', site.headers['content-length'])

file = open('out.txt', 'r')
print('File on disk: ', len(file.read()))
file.close()

file = open('out.txt', 'wb')
file.write(site.read())
site.close()
file.close()

file = open('out.txt', 'r')
print('File on disk after download: ', len(file.read()))
file.close()
print('os.stat().st_size returns: ', os.stat('out.txt').st_size)
