#!/usr/bin/env python

import socket
import struct


def bytes_to_mac(data):
    pass


def ethernet_frame(data):
    """
        This function unpack the ethernet frame and returns
        source mac, dest mac, type and payload
    """
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14]) # ! denotes it as network data
    return bytes_to_mac(dest_mac), bytes_to_mac(src_mac), socket.htons(proto), data[14:]
