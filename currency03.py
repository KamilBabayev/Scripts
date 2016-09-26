#!/usr/bin/python3

# This script will connect to central bank site and 
# get new  currency values for today

import re
from bs4 import BeautifulSoup
import urllib.request
from time import gmtime, strftime

url = 'http://cbar.az'
url_read = urllib.request.urlopen(url)
soup = BeautifulSoup(url_read, 'lxml')
time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
with open('note.txt', 'at') as f:
    f.write(time)
    f.write('\n')

result  = soup.find_all('div')
str = result[49].text

a = ['USD', 'EUR', 'RUB']
for i in range(3):
    if a[i] == "RUB":
        today_cur = re.search(r"{}\d\D\d\d\d\d".format(a[i]), str)
        d1 = today_cur.group()
        digit = re.search(r'\d\D\d\d\d\d', d1)
        print("1",a[i], digit.group(), "AZN-e beraberdir")
        with open('note.txt', 'at') as f:
            wr = a[i] + " " +  digit.group() + "\n"
            f.write(wr)
    else:
        today_cur = re.search(r"{}\d\D\d\d\d\d\d".format(a[i]), str)
        d1 = today_cur.group()
        digit = re.search(r'\d\D\d\d\d\d\d', d1) 
        print("1",a[i], digit.group(), "AZN-e beraberdir")
        with open('note.txt', 'at') as f:
            wr = a[i] + " " +  digit.group() + "\n"
            f.write(wr)

with open('note.txt', 'at') as f:
    f.write(20*'-')
    f.write("\n")

print("\n")
print('see note.txt file for old days')
