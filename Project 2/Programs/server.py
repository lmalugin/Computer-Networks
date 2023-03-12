# Project2 Server
# Lindsay Malugin
# 11.20.2022

import argparse
from pipes import quote
import socket
import random

parser = argparse.ArgumentParser()

parser.add_argument('-p', type=int, required=True)
parser.add_argument('-l', type=str, required=True)
args = parser.parse_args()

# reading quotes.txt file
quote=[]
f = open("quotes.txt", "r")
for x in f:
    quote.append(x)
f.close()

thisquote = random.choice(quote)

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #initializing the socket


IP = '10.182.0.2'
PORT = args.p
logfile = args.l


soc.bind((IP,PORT)) #binding the ip and the port of the server
listen_to = True
while listen_to:

    soc.listen(5) #letting the server accept clients
    client, address = soc.accept() #waiting for a user to connect and store the user in the client variable and them address to the adress variable
    datain = client.recv(1024).decode()
    print(datain)
    if datain=="Network": # Network is keyword
        thisquote = random.choice(quote)
        client.send(thisquote.encode()) #sending a byte string to the client.
        file = open(logfile,'a') 
        file.write(datain+"\n") 
        file.close() 

    if datain=="Quit":
       listen_to = False


client.close()
exit()