#!/usr/bin/python
file=open('mbox-short.txt')
count = 0
dict01={}
lst=[]
bigcount=None
bigname=None

for line in file:
    if line.rstrip().startswith('From '):
		lst.append(line.rstrip().split()[1])
for i in lst:
	dict01[i] = dict01.get(i,0) + 1
	for name,count in dict01.items():
		if count > bigcount:
			bigcount = count
			bigname = name
				
#print dict01
print bigname,bigcount

