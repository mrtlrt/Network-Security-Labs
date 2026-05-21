#!/usr/bin/env python3

# Task 1.3 ----------------------------------------------------
from scapy.all import *
from scapy.layers.inet import *
notReached = True
i = 1

while notReached:
  a = IP(dst='8.8.8.8', ttl=i)
  response = sr1(a/ICMP(),timeout=5,verbose=0)

  if response is None:
    print(f"{i} Timeout")
  elif response.type == 0:
    print(f"{i} {response.src}")
    notReached = False
  else:
    print(f"{i} {response.src}")
  i = i + 1