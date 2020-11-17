
from socket import *
import threading
import sys


HOST = ''  # Symbolic name meaning all available interfaces
PORT = 14594  # Arbitrary non-privileged port

serSOCK = socket(AF_INET, SOCK_STREAM)

print('Socket created')

#Bind socket to local host and port

try:

        serSOCK.bind((HOST, PORT))
except BlockingIOError as msg:
    print(msg)
    # print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print('Socket bind complete')

# Start listening on socket

serSOCK.listen(5)

print('Socket now listening')

def client_threads(connect):
    '''
    Function for handling connections. This will be used to create threads
    :param connect:
    :return:
    '''
    # Sending message to connected client
    connect.send('Welcome to the server. Type something adn hit enter\n')

    # infinite loop so function do not terminate and thread do not end.
    while True:
        # Receiving from client
        data = connect.recv(1024)
        reply = 'OK...' + data
        if not data:
            break

        connect.sendall(reply)
        # came out of loop
    connect.close()

# now keep talking with the client
while True:
    # wait to accept a  connection -- blocking call
    cliSock, addr = serSOCK.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))

    # start new thread takes 1st argument as a function name to be run,
    # second is the tuple of arguments to the function
    thread1 = threading.Thread(client_threads(cliSock))
    thread1.start()

    thread1.join()
    serSOCK.close()