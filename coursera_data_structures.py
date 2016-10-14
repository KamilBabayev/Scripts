fname = raw_input("Enter file name: ")
fd=open(fname)
count = 0
for line in fd:
    if line.rstrip().startswith('From '):
        print line.rstrip().split()[1]
        count += 1
print 'There were', count,'lines in the file with From as the first word'

#########################################

fhand = open('romeo.txt')
c = []
for line in fhand:
	line = line.rstrip().split()
	for word in lin:
		if c.count(word) == 0: c.append(word)
print(c, len(c))
