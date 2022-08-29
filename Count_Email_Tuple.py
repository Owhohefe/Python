fname = input('Enter file name\n')
try:
	fhand = open(fname)
except:
	print(fname, 'cannot be opened')
	exit()
x = dict()
for line in fhand:
	if line.startswith('From:'):
		t = line.split()
		y = t[1]
		if y not in x:
			x[y] = 1
		else:
			x[y] = x[y] + 1
#print(x)
lst = list()
for key, val in list(x.items()):
	lst.append((val, key))
lst.sort (reverse = True)
for key, val in lst[:1]:
	print(val, key)
	
