fname = input('Enter file name\n')
try:
	fhand = open(fname)
except:
	print(fname, 'cannot be opened')
	exit()
x = dict()
for line in fhand:
	if line.startswith('From '):
		t = line.split()
		y = t[5]
		v = y.split(':')
		w = v[0]
		if w not in x:
			x[w] = 1
		else:
			x[w] = x[w] + 1
#print(x)
lst = list()
for key, val in list(x.items()):
	lst.append((key, val))
lst.sort ()
for key, val in lst:
	print(key, val)