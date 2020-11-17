#!/usr/bin/env python

from socket import *

# 主机地址和端口号的默认值
DefaultHOST = 'localhost' # or '127.0.0.1'
DefaultPORT = 21041

BUFSIZ = 1024

# 允许用户指定主机和端口号
def getAddr():
    host = input('> input HOST: ')
    port = int(input('> input PORT: '))

    return host, int(port)

HOST, PORT = getAddr()

# 如果没有指定，就使用默认值
if not HOST:
    HOST = DefaultHOST

if not PORT:
    PORT = DefaultPORT

ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ').encode()
    if not data:
        break

    udpCliSock.sendto(data, ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)

    if not data:
        break

    print(data)

# udpCliSock.close()