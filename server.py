import socket
import sys


def create_socket():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print('Socket creation' + str(msg))

def bind_socket():
    try:
        global host
        global port
        global s

        print('Binding the port')

    except:



