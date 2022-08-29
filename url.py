import urllib.request 

url = input('Enter URL\n')
try:
	fhand = urllib.request.urlopen(url)
except:
	print('invalid url\n')
	exit()

count = 0
for line in fhand:
	words = line.decode().split()
	for word in words:
		for letters in word:
			count = count + 1
print(count)