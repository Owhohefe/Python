import re

reg_exp = input('Enter a regular expression\n')
fname = input ('Enter a file name\n')
try:
	fhand = open(fname)
except:
	print(Filename, 'cannot be opened')
	exit()
count = 0
for line in fhand:
	line = line.rstrip()
	if re.search(reg_exp, line):
		count = count + 1
print(fname, 'had', count, 'lines that matched', reg_exp)
		
