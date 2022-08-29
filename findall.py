import re

fname = input ('Enter a file name\n')
try:
	fhand = open(fname)
except:
	print(Filename, 'cannot be opened')
	exit()
count = 0
total = 0
for line in fhand:
	line = line.rstrip()
	x = re.findall('^New R\S*: ([0-9.]+)', line)
	if len(x) > 0:
		#print(x)
		for z in x:
			y = int (z)
			count = count + 1
			total = total + y
print(total/count)
		
