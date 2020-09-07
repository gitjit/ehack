#! /usr/bin/env python3

import subprocess
import optparse

# interface = "eth0"
# new_mac = "00:11:22:33:44:77"

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="Interface to change its MAC address")

(options, arguments) = parser.parse_args()

# interface = input("interface >")
# parser = optparse.OptionParser()
# new_mac = input("new Mac > ")

interface = options.interface
new_mac = options.new_mac

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
