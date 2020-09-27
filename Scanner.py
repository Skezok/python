#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Bienvenue dans un simple scanner de port nmap")
print("<----------------------------------------------------->")

ip_addr = input("Entrez l'IP que vous voulez scanner: ")
print("L'IP est: ", ip_addr)
type(ip_addr)

resp = input("""\nEntrez le type de scan que vous souhaitez
                1)SYN ACK Scan
                2)UDP Scan
                3)Complete Scan \n""")
print("Vous avez choisi l'option: ", resp)

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp >= '4':
    print("Veuillez entrez un numéro valide")