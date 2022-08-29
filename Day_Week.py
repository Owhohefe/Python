fname = input('Enter file name\n')
try:
	fhand = open(fname)
except:
	print('File cannot be opened')
	exit()
x = dict()
for line in fhand:
	if line.startswith('From '):
		t = line.split()
		y = t[2]
		if y not in x:
			x[y] = 1
		else:
			x[y] = x[y] + 1
print(x)
		