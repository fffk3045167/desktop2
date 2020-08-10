#!/usr/bin/env python
#!-*- coding:utf-8 -*-


from socket import *
from time import ctime


HOST = ''
PORT = 21125
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from: ', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ).decode()

        if not data:
            break
        tcpCliSock.send('[{}]{}'.format(bytes(ctime(), 'utf-8'), data).encode())

    tcpCliSock.close()

# 关闭服务器套接字(可选)
# tcpSerSock.close()