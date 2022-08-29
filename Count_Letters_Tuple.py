import string

fname = input('Enter file name\n')
try:
	fhand = open(fname)
except:
	print(fname, 'cannot be opened')
	exit()
d = dict()
intab = '0123456789'
outtab = '          '
for line in fhand:
		line = line.rstrip()
		line = line.translate(line.maketrans(intab, outtab, string.punctuation))
		line = line.lower()
		words = line.split()
		for word in words:
			for c in word:
				if c not in d:
					d[c] = 1
				else:
					d[c] = d[c] + 1
#print(d)
lst = list()
for key, val in list(d.items()):
	lst.append((val, key))
lst.sort (reverse = True)
for key, val in lst:
	print(val, key)
