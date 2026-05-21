#!/usr/bin/env python3

# Task 1.2 ----------------------------------------------------
from scapy.all import *
from scapy.layers.inet import *

a = IP()
a.src = '10.20.30.40'
a.dst = '10.9.0.6'
b = ICMP()
p = a/b


ls(a)
send(p)


