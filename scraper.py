#!/usr/bin/env python
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError

url = 'http://atl.az'
def scrap(url):
    html = urlopen(url)
    bsobj = BeautifulSoup(html, 'lxml')
    data1 = bsobj.title
    data2 = bsobj.li
    print(data1)
    print(data2)
    
scrap(url)