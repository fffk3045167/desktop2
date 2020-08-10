#!/usr/bin/env python

from socketserver import TCPServer as TCP
from socketserver import StreamRequestHandler as SRH
from time import ctime

HOST = 'localhost'
PORT = 18645
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print('...connected from: ', self.client_address,
              self.wfile.write('[{}]{}'.format(ctime(),
                self.rfile.readline()).encode()))


tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()