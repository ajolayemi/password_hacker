#!/usr/bin/env python

import socket

# The following host is a standard loopback
# interface address which is also the localhost
HOST = '127.0.0.1'
# Port can be between 0 - 65535 with 0 being a reserved port
# In some systems as well, ports from 0 - 1023 are system reserved
PORT = 65432

# socket.AD_INET is one of internet address family and this represents IPv4
# address family
# socket.SOCK_STREAM is the socket type for Transmission Control Protocol (TCP)


def server_socket(host=HOST, port=PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as s:
        # bind() associates a socket with a specific network interface and port number
        s.bind((host, port))
        # listen() enables a server to accept() connections.
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                # Read data sent by client socket
                data = conn.recv(1024)
                if not data:
                    break
                # Send all data back to server socket
                conn.sendall(data)


if __name__ == '__main__':
    server_socket()