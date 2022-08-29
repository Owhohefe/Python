import socket

s = socket.socket()

s.connect(("10.10.15.1", 22))

answer = s.recv(1024)

print(answer)

s.close
