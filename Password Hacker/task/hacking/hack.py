#!/usr/bin/env python

import socket
import argparse

DESCRIPTION = 'Connects to an unprotected admin website '


def cli_parser():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('-ip', '--ip_address',
                        help='Enter the IP address for the admin website')
    parser.add_argument('--port',
                        help='Enter the port to be used.')
    parser.add_argument('-msg', '--message_for_sending',
                        help='Enter the msg needed to connect to admin website')
    return parser.parse_args()


class SocketHandler:
    """ Creates and manages both server and clients socket servers. """

    def __init__(self, host, port, msg: str):
        self.host = host
        self.port = port
        self.msg = msg.encode('utf-8')
        self.conn_success = False
        self.address = (self.host, self.port)

    def server_socket(self):
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


if __name__ == '__main__':
    cli_parser()
