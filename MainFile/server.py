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
    while True:
        try:
            message = client.recv(1024)
            boardcast(message)
        except:
            index = client.index(client)
            client.remove(client)
            client.close()
            nickname = nicknames[index]
            boardcast(f"{nickname} left the chat!".encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connect with {str(address)}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nicknames}!")
        boardcast(f'{nickname} joined the chat'.encode('ascii'))
        client.send('connect to the server!'.encode('ascii'))

        thread = threading.Thread(target=handel, args = (client,))
        thread.start()
print("-"*3,"Server is started..!!","-"*3)
receive()
