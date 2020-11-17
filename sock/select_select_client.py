# coding: utf-8

from socket import *


# 主机地址和端口号的默认值
HOST = 'localhost' # or '127.0.0.1'
PORT = 21125
BUFSIZ = 1024
ADDR = (HOST, PORT)

messages = ['This is the message ', 'It will be sent ', 'in parts', ]

tcpClient = [socket(AF_INET, SOCK_STREAM), socket(AF_INET, SOCK_STREAM)]

# 将套接字连接到服务器监听的端口
print ('connecting to %s port %s' % ADDR)

for sock in tcpClient:
    sock.connect(ADDR)

for index, message in enumerate(messages):
    # 在两个套接字上发送消息
    for sock in tcpClient:
        print('{}: sending "{}"'.format(sock.getsockname(), message + str(index)))
        sock.send((message + str(index)).encode())

for sock in tcpClient:
    data = sock.recv(BUFSIZ)
    print('{}: received "{}"'.format(sock.getsockname(), data))
    if data != '':
        print('closing socket', sock.getsockname())
        sock.close()