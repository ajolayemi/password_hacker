#!/usr/bin/env python
import socket
import argparse
import string
import random

DESCRIPTION = 'Connects to an unprotected admin website '
alpha = ''.join((string.ascii_lowercase, string.digits))


def cli_parser():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('ip',
                        help='Enter the IP address for the admin website')
    parser.add_argument('port', type=int,
                        help='Enter the port to be used.')
    return parser.parse_args()


class SocketHandler:
    """ Creates and manages both server and clients socket servers. """

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.address = (self.host, self.port)

    @staticmethod
    def gen_pass():
        return ''.join(random.choice(alpha) for _ in range(random.randint(1, 3)))

    def client_socket(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect(self.address)
            while True:
                generated_pass = self.gen_pass()
                client.sendall(generated_pass.encode('utf-8'))
                server_msg = client.recv(1024)
                if server_msg.decode('utf-8') == 'Connection success!':
                    print(generated_pass)
                    break


def main():
    args = cli_parser()
    socket_class = SocketHandler(host=args.ip, port=args.port)
    socket_class.client_socket()


if __name__ == '__main__':
    main()
