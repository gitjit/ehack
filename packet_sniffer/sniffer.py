#!/usr/bin/env python

import socket
import struct
import sys


def main():
    print(sys.version)
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        raw_data, addr = conn.recvfrom(65536)
        print(raw_data)


def bytes_to_mac(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str)


def ethernet_frame(data):
    """
        This function unpack the ethernet frame and returns
        source mac, dest mac, type and payload
    """
    dest_mac, src_mac, proto = struct.unpack(
        '! 6s 6s H', data[:14])  # ! denotes it as network data
    return bytes_to_mac(dest_mac), bytes_to_mac(src_mac), socket.htons(proto), data[14:]


# print(bytes_to_mac(b"000100100011010001010110011110001001101010111100"))

main()
