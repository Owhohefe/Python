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
		if y not in x:
			x[y] = 1
		else:
			x[y] = x[y] + 1
print(x)
largest = None
smallest = None
for key in x:
	if  largest is None or x[key] > largest:
		largest = x[key]
for key in x:
	if  smallest is None or x[key] < smallest:
		smallest = x[key]
print('Largest:', largest)
print('Smallest:', smallest)
			