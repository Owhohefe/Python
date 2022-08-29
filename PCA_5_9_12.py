from os import strerror

data = bytearray(10)

try:
    bf = open('file.bin', 'rb')
    bf.readinto(data)
    bf.close()

    for i in data:
        print(int(i),end=" ")

    print("completed")
	
except IOError as e:
    print("I/O error occurred: ", strerr(e.errno))
