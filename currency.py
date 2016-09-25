#!/usr/bin/python3

# This script will connect to central bank site and 
# get new USD currency for today

import re
from bs4 import BeautifulSoup
import urllib.request

url = 'http://cbar.az'
url_read = urllib.request.urlopen(url)
soup = BeautifulSoup(url_read, 'lxml')

result  = soup.find_all('div')
str = result[49].text

today_cur = re.search(r'USD\d\D\d\d\d\d\d', str)
d1 = today_cur.group()
digit = re.search(r'\d\D\d\d\d\d\d', d1)
print("1 USD", digit.group(), "AZN-e beraberdir")

today_cur = re.search(r'EUR\d\D\d\d\d\d\d', str)
d2 = today_cur.group()
digit = re.search(r'\d\D\d\d\d\d\d', d2)
print("1 EUR", digit.group(), "AZN-e beraberdir")

today_cur = re.search(r'RUB\d\D\d\d\d\d', str)
d3 = today_cur.group()
digit = re.search(r'\d\D\d\d\d\d', d3)
print("1 RUBL", digit.group(), "AZN-e beraberdir")
