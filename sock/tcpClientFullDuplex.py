#!-*- coding:utf-8 -*-

from socket import *
from select import select
import sys

HOST = "localhost"
PORT = 9898
ADDR = (HOST, PORT)
BUFSIZE = 1024



def prompt():
    sys.stdout.write('<You> ')
    sys.stdout.flush()

def gen_message(room_id, raw_message):
    return '<RID:{}>{}</RID:{}>'.format(room_id, raw_message, room_id)


def main():
    room_id = input('<Room ID> ')

    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.settimeout(2)
    _current_in_list = [tcpCliSock]

    try:
        tcpCliSock.connect(ADDR)
        _current_in_list.append(tcpCliSock)

        # notify all room's user that new client is entered
        tcpCliSock.send(gen_message(room_id, '').encode())
    except (BlockingIOError, ConnectionResetError):
        print("Unable to connect")
        sys.exit()

    print('Connected to remote host. Start sending messages')
    prompt()

    while True:
        rlist, wlist, xlist = select(_current_in_list, [], _current_in_list)
        for sock in rlist:
            if sock is tcpCliSock:
                message = sock.recv(BUFSIZE)
                if not message:
                    print('\nDisconnected from chat server.')
                    sys.exit()
                else:
                    sys.stdout.write(message)
                    prompt()
            else:
                raw_message = sys.stdin.readline()
                tcpCliSock.send(gen_message(room_id, raw_message).encode())
                prompt()


if __name__ == '__main__':
    main()