#!-*- coding:utf-8 -*-

from socket import *
from select import select
import queue
from time import sleep

# 主机地址和端口号的默认值
HOST = 'localhost' # or '127.0.0.1'
PORT = 21125
BUFSIZ = 1024
ADDR = (HOST, PORT)

# 创建服务器套接字
tcpServer = socket(AF_INET, SOCK_STREAM)

# 将socket设置为非阻塞. 在创建socket对象后就进行该操作
# 由于普通的server-socket一次只能处理一个client-socket.因为socket在
# accept等待接收和recv等待数据数据时都会阻塞, 每次处理client只能应对一个socket.
# tcpServer.setblocking(False)
# 套接字与地址绑定
tcpServer.bind(ADDR)
# 监听连接
tcpServer.listen(5)

# 套接字的读取列表
inputs = [tcpServer]
# 写入套接字，处理要发送的消息
outputs = []
# 输出消息队列
message_queues = {}

# 开始循环
while inputs:
    #  Wait for at least one of the sockets to be ready for processing
    print('waiting for the next event')

    try:
        # 开始select监听,对inputs中的服务端socket进行监听
        # 一旦调用socket的send, recv函数,将会再次调用次模块
        readable, writable, exceptional = select(inputs, outputs, inputs)
    except BlockingIOError:
        pass

    # 接收消息！！！
    # 当有客户端连接进来时 select 将触发
    for sock in inputs:

        try:
            # 判断当前触发的是不是服务端对象, 当触发的对象是服务端对象时,
            # 说明有新客户端连接进来了，表示有新用户连接
            if sock is tcpServer:
                # 一个服务器 socket 已经准备好接受连接
                tcpClient, client_address = sock.accept()
                print('...connected from: ', client_address)
                tcpClient.setblocking(False)
                # 将客户端对象也加入到监听列表中，当客户端发送消息时, select将触发
                inputs.append(tcpClient)

                # 为连接的客户端单独创建一个消息队列，用来保存客户端发送的消息
                message_queues[tcpClient] = queue.Queue()
            else:
                # 由于客户端连接进来时服务端接收客户端连接请求，将客户端加入到了监听列表中(inputs)
                # 客户端发送消息将触发,所以判断是否是客户端对象触发
                # 有老用户发消息，处理接受
                data = sock.recv(BUFSIZ)
                # 如果客户端未断开
                if data != '':
                    print('received {} from {}'.format(data, sock.getpeername()))
                    # 将收到的消息放入相对应的socket客户端的消息队列中
                    message_queues[sock].put(data)
                    # 然后将需要进行回复操作的socket放到outputs列表中，让select监听
                    if sock not in outputs:
                        outputs.append(sock)

                else:
                    # 客户端断开了连接，将客户端的监听从inputs 列表中移除
                    print('closing', client_address)
                    # 停止监听tcpclient
                    if sock in outputs:
                        outputs.remove(sock)
                    inputs.remove(sock)
                    # 关闭socket
                    sock.close()

                    # 移除对应socket客户端对象的消息队列
                    del message_queues[sock]
        except (BlockingIOError, ConnectionResetError):
            pass

    # 发送消息！！！
    # 如果现在没有客户端请求，也没有客户端发送消息，那就开始对发送消息列表进行处理
    # 以及是否需要发送消息，存储哪个客户端发送过消息
    for sock in writable:
        try:
            # 如果消息队列中有消息,从消息队列中获取要发送的消息
            message_queue = message_queues.get(sock)
            send_data = ''
            if message_queue is not None:
                send_data = message_queue.get_nowait()
            else:
                # 客户端连接断开了
                print('has closed ')
        except queue.Empty:
            # 客户端连接断开了
            print('{}'.format(sock.getpeername()))
            outputs.remove(sock)
        else:
            # print "sending %s to %s " % (send_data, s.getpeername)
            # print "send something"
            if message_queue is not None:
                sock.send(send_data)
            else:
                print('has closed')

            # del message_queues[s]
            # writable.remove(s)
            # print "Client %s disconnected" % (client_address)

    # 处理异常的情况
    for sock in exceptional:
        print('exception condition on', sock.getpeername())
        # Stop listening for input on the connection
        inputs.remove(sock)
        if sock in outputs:
            outputs.remove(sock)

        sock.close()

        # remove message queue
        del message_queues[sock]

    sleep(1)