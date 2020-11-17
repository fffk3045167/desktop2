#!/usr/bin/env python
#!-*- coding:utf-8 -*-

from socket import *


HOST = 'localhost' # or '127.0.0.1'
PORT = 21325
BUFSIZ = 1024

ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ').encode()  # 将str转码为bytes

    if not data:
        break

    # 向服务器发送消息
    tcpCliSock.send(data)
    # 接收来自服务器的消息
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break

    print(data.decode('utf-8'))

# 关闭客户端套接字(可选)
# tcpCliSock.close()