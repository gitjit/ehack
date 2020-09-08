#!/usr/bin/env python3
import scapy.all as scapy
import optparse
import re


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--ip", dest="ip", help="IP Range for Arp request in CIDR format eg: 10.0.2.1/24")
    options, arguments = parser.parse_args()
    return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)  # Create an ARP request
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # Create a Ethernet broadcast packet
    arp_request_broadcast = broadcast / arp_request
    # answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1)
    # print(answered_list.summary())
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    print("IP \t\t\t\t Mac Address\n-----------------------------------")
    clients_list = []
    for answer in answered_list:
        client_dict = {"ip": answer[1].psrc, "mac": answer[1].hwsrc}
        clients_list.append(client_dict)

    print_result(clients_list)


def print_result(results):
    for result in results:
        print(result["ip"] + "\t\t" + result["mac"])


options = get_args()

if options.ip:
    ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:/\d{1,2}|)", options.ip)
    if ip:
        print(ip.group(0))
        scan(ip.group(0))  # scan("10.0.2.1/24")
    else:
        print('Invalid IP Range')



