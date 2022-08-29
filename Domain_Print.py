fname = input('Enter file name\n')
try:
	fhand = open(fname)
except:
	print('File cannot be opened')
	exit()
x = dict()
for line in fhand:
	if line.startswith('From:'):
		t = line.split()
		y = t[1]
		z = y.index('@')
		p = y[z:]
		if p not in x:
			x[p] = 1
		else:
			x[p] = x[p] + 1
print(x)