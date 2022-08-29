fname = input('Enter the file name\n')
try:
	fhand = open(fname)
except:
	print('You must enter a valid file name\n')
	exit()
x = dict()
for line in fhand:
	t = line.split()
	for word in t:
		x [word] = ' '
print(x)
print('\n\n')
h = 'one' in x
print(h)
	