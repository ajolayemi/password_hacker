#!/usr/bin/env python

import socket
import argparse
import sys

DESCRIPTION = 'Connects to an unprotected admin website '


def cli_parser():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('ip',
                        help='Enter the IP address for the admin website')
    parser.add_argument('port', type=int,
                        help='Enter the port to be used.')
    parser.add_argument('msg',
                        help='Enter the msg needed to connect to admin website')
    return parser.parse_args()


class SocketHandler:
    """ Creates and manages both server and clients socket servers. """

    def __init__(self, host, port, msg: str):
        self.host = host
        self.port = port
        self.msg = msg.encode('utf-8')
        self.address = (self.host, self.port)

    def client_socket(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect(self.address)
            client.sendall(self.msg)
            server_msg = client.recv(1024)
        print(server_msg.decode('utf-8'))

    def server_socket(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
                server.bind(self.address)
                server.listen()
                con, address = server.accept()
                with con:
                    while True:
                        # Receive data send by user
                        user_data = server.recv(1024)
                        if not user_data:
                            break
                        server.sendall('Wrong Password!'.encode('utf-8'))
        except KeyboardInterrupt:
            sys.exit()


def main():
    args = cli_parser()
    socket_class = SocketHandler(host=args.ip, port=args.port,
                                 msg=args.msg)
    socket_class.client_socket()


if __name__ == '__main__':
    main()
