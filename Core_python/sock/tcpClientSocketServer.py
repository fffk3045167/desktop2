#!/usr/bin/env python

from socket import *

HOST = 'localhost'
PORT = 18645
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('> ')
    if not data:
        break

    tcpCliSock.send(('{}\r\n'.format(data)).encode())
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break

    print(data.strip())

# tcpCliSock.close()