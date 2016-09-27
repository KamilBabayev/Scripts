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
#soup.ul.li.a.next  # Example traversing

time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
with open('note.txt', 'at') as f:
    f.write(time)
    f.write('\n')

result  = soup.find_all('span', class_="item item_4")

usd,eur,rub = result[0].text,result[1].text,result[2].text
usd = "1 USD: " +  " " + usd
eur = "1 EUR: " +  " " + eur
rub = "1 RUB: " +  " " + rub
cur_list = [usd,eur,rub]
for cur in cur_list:
    print(cur)

with open('note.txt', 'at') as f:
    for  cur in cur_list:
        f.write(cur)
        f.write('\n')
    f.write(20*'-')
    f.write("\n")

print("\n")
print('see note.txt file for old days')
