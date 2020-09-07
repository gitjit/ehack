#! /usr/bin/env python3
#This program changes the mac address of the specified interface (eth0).
# You have to supply interface name (interface = "eth0") and new  mac address ("00:11:22:33:44:77")

import subprocess
import optparse
import  re


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="Interface to change its MAC address")
    options, arguments = parser.parse_args()
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(['ifconfig', interface])
    mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address:
        return mac_address.group(0)
    else:
        return None


options = get_args()
current_mac = get_current_mac(options.interface)
if current_mac:
    print('Current mac is ' + current_mac)

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac:
    print('Current mac is ' + current_mac)

