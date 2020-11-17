from socket import *
from time import ctime
import select 
import sys

HOST = ''
PORT = 12346
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpServer = socket(AF_INET, SOCK_STREAM)
tcpServer.bind(ADDR)
tcpServer.listen(5)
gets = [tcpServer, sys.stdin]

while True:
    print('Waiting for connection...')
    tcpClient, addr = tcpServer.accept()
    print('...connected from: ', addr)
    gets.append(tcpClient)

    while True:
        readyInput, readyOutput, readyException = select.select(gets, [], [])
        for indata in readyInput:
            if indata == tcpClient:  
                data = tcpClient.recv(BUFSIZE)
                if not data:
                    break
                print('[%s]: %s' % (ctime(), data.decode('utf-8')))
            else:
                data = input('> ')
                if not data:
                    break
                tcpClient.send(bytes(data, 'utf-8'))
    tcpClient.close()

# 关闭服务器套接字(可选)
# tcpServer.close()