import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)



scan("10.10.14.212/24")
