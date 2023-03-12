# Project2 Client
# Name: Lindsay Malugin
# Date: 11.20.2022

import sys
import argparse
import socket

# Parsing IP, port, and logfile
parser = argparse.ArgumentParser()
parser.add_argument('-s', type=str, required=True)
parser.add_argument('-p', type=int, required=True)
parser.add_argument('-l', type=str, required=True)
args = parser.parse_args()


HOST = args.s
PORT = args.p
logfile = args.l


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #initializing the socket
client.connect((HOST,PORT))
data = "Network"
client.send(data.encode())
data = client.recv(1024)
client.close()

print(data.decode())

file = open(logfile,'a') 
file.write(str(data.decode())) 
file.close() 