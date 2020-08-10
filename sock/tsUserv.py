#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 21041
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for message...')

    data, addr = udpSerSock.recvfrom(BUFSIZ)
    data = data.decode()
    udpSerSock.sendto('[{}] {}'.format(ctime(), data).encode(), addr)

    print('...received from and returned to: ', addr)

# udpSerSock.close()
