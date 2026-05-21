#!/usr/bin/python3
from scapy.all import *
from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import IP, UDP

Qdsec = DNSQR(qname="rando.example.com")
dns = DNS(id=0xAAAA, qr=0, qdcount=1, ancount=0, nscount=0, arcount=0, qd=Qdsec)
ip = IP(dst="10.9.0.53", src="1.3.5.9")
udp = UDP(dport=53, sport=52055, chksum=0)
request = ip/udp/dns

#send(request)

with open("ip_req.bin", "wb") as f: # write the request to a file
	f.write(bytes(request))