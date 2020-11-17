#!/usr/bin/env python
#!-*- coding:utf-8 -*-

from socket import *


HOST = ''
PORT = 21325
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
        # 接收来自客户端的消息
        data = tcpCliSock.recv(BUFSIZ).decode()

        if not data:
            break

        print(data)

        serv_msg = input('> ').encode()
        # 向客户端发送消息
        tcpCliSock.send(serv_msg)


    tcpCliSock.close()

# 关闭服务器套接字(可选)
# tcpSerSock.close()