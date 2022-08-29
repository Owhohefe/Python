from os import strerror

data = bytearray(10)
for i in range(len(data)):
	data[i] = 10 + i
try:
	bf = open('file.bin', 'wb')
	bf.write(data)
	bf.close()
	print("completed")
except IOError as e:
	print("I/O error occurred: ", strerr(e.errno))
