#!/usr/bin/env python

import socket

# The following host is a standard loopback
# interface address which is also the localhost
HOST = '127.0.0.1'
# Port can be between 0 - 65535 with 0 being a reserved port
# In some systems as well, ports from 0 - 1023 are system reserved
PORT = 65432


def client_socket(server_host=HOST, server_port=PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_host, server_port))
        s.sendall('Hello world'.encode('utf-8'))
        data = s.recv(1024)
    print('Received', repr(data))


if __name__ == '__main__':
    client_socket()