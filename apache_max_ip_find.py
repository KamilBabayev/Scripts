#!/usr/bin/env python3
#  This python script analyzes access.log file 
#  and finds ip addresses per try amounts. Then we can
#  decide what to do with this ip addresses. ex: ban vi firewall
counts = {}
with open('/var/log/httpd/access.log') as file:
	for name in file:			
		line = name.rstrip().split()
		counts[line[0]] = counts.get(line[0], 0) + 1
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))
lst.sort(reverse=True)
for val, key in lst:
    print(key, val)
