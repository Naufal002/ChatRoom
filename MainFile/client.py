import threading
import socket

import os
os.system('cls')

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def receive():
    while True:
        try:
            messages = client.recv(1024).decode('ascii')
            if messages == 'NICK':
                client.send(nickname.endcode('ascii'))
            else:
                print(messages)
        except:
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        messages = f'{nickname}: {input("")}'
        client.send(messages.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()