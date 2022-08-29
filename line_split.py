fname = input ("Enter file name\n")
try:
	fhand = open(fname)
except:
	print('file cannot be opened')
	exit()
x = []
for line in fhand:
	t = line.split()
	for word in t:
		if word in x: continue
		x.append(word)
x.sort()
print (x)