import socket
import sys

backlog = 1
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.8.136', 5005))
s.listen(1)

try:
    print ("is waiting")
    client, address = s.accept()

    while 1:
        data = client.recv(size)
        if data:
            print (data)

finally:
    print("closing socket")
    cient.close()
    s.close()
