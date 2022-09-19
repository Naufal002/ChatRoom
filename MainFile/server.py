import threading
import socket
import os
os.system('cls')

host = '127.0.0.1' #localhost
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []
nicknames = []

def boardcast(message):
    for client in clients:
        client.send(message)

def handel(client):
    try:
        message = client.recv(1024)
        boardcast(message)
    except:
        index = client.index(client)