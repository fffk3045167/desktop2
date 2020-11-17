#!/usr/bin/env python
#!-*- coding:utf-8 -*-

from socket import *

# 主机地址和端口号的默认值
DefaultHOST = 'localhost' # or '127.0.0.1'
DefaultPORT = 21125

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

#print(HOST, PORT)
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