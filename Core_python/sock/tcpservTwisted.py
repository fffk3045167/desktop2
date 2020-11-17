#!/usr/bin/env/ python

from twisted.internet import protocol, reactor
from time import ctime

PORT = 23145

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...connection from: ', clnt)

    def dataReceived(self, data):
        self.transport.write('[{}]{}'.format(ctime(), data).encode())

factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connection...')
reactor.listenTCP(PORT, factory)
reactor.run()