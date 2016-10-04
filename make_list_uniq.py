#!/usr/bin/python3

a = [2,3,4,55,3,100,100,33,44,55,100,3,4,4,4,4,4]
print(a)
for i in range(len(a)):
	b = a[1+i:]
	for x  in b:
		if a[i] == x:
			print(a[i])
			a.remove(a[i])
print(a)
