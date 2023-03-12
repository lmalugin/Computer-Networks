# 4200 Program1 : Sockets Program: Creating a socket connection for the client.
# Name: Lindsay Malugin
# Date: 10.21.2022

import sys
import argparse
import socket

# This block of code is used to parse command-line options and arguments. Formatting the output to look like "-s xxx.xxx.xxx.xxx -p xxxx -l logfile".
parser = argparse.ArgumentParser()
parser.add_argument('-s', type=str, required=True)  #Host
parser.add_argument('-p', type=int, required=True)  #Port
parser.add_argument('-l', type=str, required=True)  #Logfile
args = parser.parse_args()

HOST = args.s
PORT = args.p
logfile = args.l

# Creating client connection 
client = socket.socket()
client.connect((HOST,PORT))
client.send('Network'.encode())  # Sending the keyword "Network" to the server in order to receive the key phrase needed
data = client.recv(1024)
client.close()  # Closing connection


# Log file processing
file = open(logfile,'w')
file.write(str(data.decode()))
file.close()