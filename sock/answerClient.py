from socket import *
from time import ctime
import select
import sys

HOST = 'localhost'
PORT = 12346
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpClient = socket(AF_INET, SOCK_STREAM)
tcpClient.connect(ADDR)
gets = [tcpClient, sys.stdin]

while True:
    readyInput, readyOutput, readyException = select.select(gets, [], [])
    for indata in readyInput:
        if indata == tcpClient:
            data = tcpClient.recv(BUFSIZE)
            if not data:
                break
            print('[%s]: %s' % (ctime(), data.decode('utf-8')))
        else:
            data = input()
            if not data:
                break
            tcpClient.send(bytes(data, 'utf-8'))

#
# tcpClient.close()