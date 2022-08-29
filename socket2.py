import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = input('Enter URL\n')
try:
	x = url.split('/')
	y = x[2]
	mysock.connect((y, 80))
except:
	print('invalid url\n')
	exit()
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

mysock.send(cmd)
count = 0
total = 0
while True:
    data = mysock.recv(512)
    total = total + len(data)
    if len(data) < 1 or total >= 3000:
        break
    y = data.decode()
    #print(y)
    v = y.split()
    for words in v:
       for letters in words:
          count = count + 1
          #print(letters, count)
print(count)
	
	#print(data.decode(),end='')

mysock.close()