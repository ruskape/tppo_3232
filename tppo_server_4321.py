#!/usr/bin/env python3

import socket 
import sys
import re
import os
import json
from datetime import datetime


fname = 'data.json'


def reload(history):
    try:
        data = json.load(open('data.json'))
    except:
        data = []
    data.append(history)
    with open('data.json', 'w') as data_file:
        json.dump(data, data_file, indent = 2, ensure_ascii=False)
        #data_file.write('\n')
    print('Information is saved to data.json')

HOST = '0.0.0.0'                        
PORT = 12342                 
s = None

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(10)
    print("Hello! Let's strart!")
except socket.error as e:
    if s: s.close()
    print(f'ERROR: {e}')
    sys.exit(1)


while True:
    s2 = s.accept()
    pid = os.fork()
    if pid != 0:
        continue
    sock, remote = s2
    try: 
        line = sock.recv(2050).decode()

        if line == '':
            print('Empty message!')

        elif line == 'information':
            if not os.path.exists('data.json'):
                sock.send(b'brightness: 0; color: 0,0,0')
            else: 
                data = json.load(open('data.json'))
                st = str(data[-1])
                print(st)
                sock.send(st.encode())
                print('Send information to clinet')

        else:
            print('Request to change lamp settings received:', line)
            
            line = line.rstrip()
            res = re.split(r' ', line)
            time = str(datetime.now())
            history = {'time':time, 'brightness':res[1], 'color':res[3]}
            reload(history)
            sock.send(b'Lamp parameters have been changed!')
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
            break
    
    except socket.error as e:
        if s: s.close()
        print(f'ERROR: {e}')
        sys.exit(1)


