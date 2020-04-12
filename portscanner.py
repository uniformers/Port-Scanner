#!/usr/bin/env python
import socket
import os
os.system('color')
from termcolor import colored

#create a socket object to scan an IPV4 Addr using TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# enter the ip address of the host to scan
host = input("[*] Enter the host to scan: ")

def portscanner(port):
    if sock.connect_ex((host,port)):
        print(colored("[!!] Port %d is closed " % (port), 'red'))
    else:
        print(colored("[+] Port %d is open " % (port), 'green'))

for port in range (1,450):
    portscanner(port)



