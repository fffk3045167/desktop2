#!-*- coding:utf-8 -*-

from socket import *
from select import select
import re

HOST = ''
PORT = 9898
BUFSIZE = 1024
ADDR = (HOST, PORT)


CONFORM_MSG = re.compile(r'^<RID:(\d+)>([\s\S]*?)</RID:\1>')

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

tcpSerSock.setblocking(False)

_current_in_list = [tcpSerSock]
_room = {}

def broadcast_message(room_id, sock, message):
    for member in _room[room_id]:
        if member is not sock:
            try:
                member.send(message)
            except (BlockingIOError, ConnectionResetError):
                member.close()
                _current_in_list .remove(member)
                _room[room_id].remove(member)


def main():
    while True:
        rlist, wlist, xlist = select(_current_in_list, [], [])

        for sock in rlist:
            if sock is tcpSerSock:
                client, addr = sock.accept()
                _current_in_list.append(client)
                print("Client ({}:{}) connected.".format(client, addr))

            else:
                try:
                    raw_message = sock.recv(BUFSIZE)
                    if raw_message:
                        rgx_message = CONFORM_MSG.match(raw_message.decode())
                        if rgx_message:
                            room_id = rgx_message.group(1)
                            message = rgx_message.group(2)
                            if sock not in _room.setdefault(room_id, []):
                                _room[room_id].append(sock)
                                broadcast_message(room_id, sock, '\n[%s:%s] entered room.\n'\
                                                                         % sock.getpeername())
                            else:
                                broadcast_message(room_id, sock,
                                                "\n<" +str(sock.getpeername()) + ">" + message)
                        else:
                            print("Invalid format message,", raw_message)
                except (BlockingIOError, ConnectionResetError):
                    print("Client (%s, %s) is offline" % sock.getpeername())
                    _current_in_list .remove(sock)
                    for room_id, socks in _room.items():
                        for _ in socks:
                            if _ is sock:
                                _room[room_id].remove(_)
                                break
                        else:
                            continue
                        break


if __name__ == '__main__':
    main()