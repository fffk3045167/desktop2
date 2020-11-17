#!/usr/bin/env python
#!-*- coding:utf-8 -*-


from socket import *
from time import ctime
import os


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
        # 接收来自客户端的消息
        data = tcpCliSock.recv(BUFSIZ).decode()

        if not data:
            break
        # os.name 获取操作系统信息(posix,nt,java,对应linux/windows/java虚拟机)
        # 向客户端发送消息
        tcpCliSock.send('[{}],[{}] {}'.format(
            ctime(), os.name, data).encode())


    tcpCliSock.close()

# 关闭服务器套接字(可选)
# tcpSerSock.close()