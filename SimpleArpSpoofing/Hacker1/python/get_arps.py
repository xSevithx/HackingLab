#!/usr/bin/python
from scapy.all import *   
import sys, socket   
import argparse
import os
if os.geteuid() != 0:
	exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")
parser = argparse.ArgumentParser(description='List MAC address in a given range.')
parser.add_argument('-t', dest='target',help='Target IP Address', required=True)
parser.add_argument('-i', dest='iface',help='Interface', required=True)
args = parser.parse_args()

conf.verb=1 
conf.iface=args.iface
destination=args.target
ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=destination),timeout=2)
for snd,rcv in ans:
    print(rcv.sprintf(r"%Ether.src% at address %ARP.psrc%"))