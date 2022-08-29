import socket

ports = [22,23,25,3306]

for i in range (0,4):

    s = socket.socket()

    port = ports[i]

    print ('This is the Banner for the port')

    print (port)

    s.connect(("45.33.32.156", port))

    answer = s.recv(1024)

    print(answer)

    s.close
