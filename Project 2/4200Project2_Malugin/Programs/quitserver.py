# Program : Shut Down Sockets Server Program
# Name: Lindsay Malugin
# Date: 11.20.2022
import sys
import argparse
import socket

parser = argparse.ArgumentParser()
parser.add_argument('-s', type=str, required=True)
parser.add_argument('-p', type=int, required=True)
args = parser.parse_args()


HOST = args.s
PORT = args.p


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))
data = "Quit"
client.send(data.encode())
data = client.recv(1024)
client.close()
