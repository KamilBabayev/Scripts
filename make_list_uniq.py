#!/usr/bin/python3

a = [2,3,4,55,3,100,100,99,333,22,2,2]
print('original list: ',a)
for i in range(len(a)):
	b = a[1+i:]
#	print(b)
	for x in b:
		if a[i] == x:
			a.remove(a[i])
print('uniques: ',a)

a = [2,3,4,55,3,100,100]
c=[]
for i in range(len(a)):
    b = a[1+i:]
#    print(b)
    for x in b:
        if a[i] == x:
            c.append(a[i])
print("Non uniques: ", c*2)
