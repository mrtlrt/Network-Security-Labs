#!/usr/bin/env python3
from scapy.all import *

def print_pkt(pkt):
  pkt.show()

#Task 1.1A/B part 1
#pkt = sniff(iface='br-5f9aa6b242e3', filter='icmp', prn=print_pkt)

#Task 1.1B part 2
#pkt = sniff(iface='br-5f9aa6b242e3', filter='tcp && src host 10.9.0.6 && dst port 23', prn=print_pkt)

#Task 1.1B part 3
pkt = sniff(iface='br-5f9aa6b242e3', filter='net 128.230.0.0/16', prn=print_pkt)


