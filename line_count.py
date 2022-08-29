fname = input ("Enter file name\n")
try:
	fhand = open(fname)
except:
	print('file cannot be opened')
	exit()
count = 0
for line in fhand:
	if line.startswith('From '):
		t = line.split()
		print(t[1])
		count = count+1
print('There were ', count, ' lines in the file with from as the first word')
