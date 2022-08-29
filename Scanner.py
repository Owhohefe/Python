#!/bin/python

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("invalid number of arguments")
    print("python3 Scanner.py <ip>")

print("-" * 50)
print("scanning target "+ target)
print("Time started: "+ str(datetime.now()))
print("-" * 50)

try:
    for port in range(1,200):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print("port {} is open".format(port))
        else:
            print("port {} is closed".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting program")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

except socket.error:
    print("couldn't connect to server")
    sys.exit()
    

print("Time ended: "+ str(datetime.now()))

