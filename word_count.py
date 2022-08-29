fname = input ("Enter file name\n")
try:
	fhand = open(fname)
except:
	print('file cannot be opened')
	exit()
count = 0
for line in fhand:
    line = line.rstrip()
    t = line.split()
    for word in t:
        count = count+1
print(count)
