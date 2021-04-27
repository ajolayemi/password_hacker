#!/usr/bin/env python

import socket
import argparse

DESCRIPTION = 'Pass in the required arguments. '


def cli_parser():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('-ip', '--ip_address',
                        help='Enter the IP address for the admin website')
    parser.add_argument('--port',
                        help='Enter the port to be used.')
    parser.add_argument('-msg', '--message_for_sending',
                        help='Enter the msg needed to connect to admin website')
    return parser.parse_args()

