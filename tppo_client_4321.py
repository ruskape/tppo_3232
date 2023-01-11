import socket, sys

def RGB(str):
    try:
        str = str.split(',')
        i = 0
        for l in str:
            if int(l) >=0 and int(l) < 256:
                i += 1
        if i != 3:
            return False
        else: 
            return True
    except: 
        print("ERROR: Color entered incorrectl")
        exit()

s = socket.socket(
    socket.AF_INET, 
    socket.SOCK_STREAM
)

s.connect(
    ('0.0.0.0', 12342)
)
boofer = bytearray()
#brightness
if len(sys.argv) > 2 and sys.argv[1] == '-b':
    if sys.argv[2].isdigit:
        if int(sys.argv[2]) > 0 and int(sys.argv[2]) < 11:
            i = 1
        else:
            print('ERROR: Brightness should be in the range 1..10')
            exit()
    else:
        print('ERROR: The brightness level must be entered as a number from 1 to 10')
        exit()

elif len(sys.argv) > 0 and sys.argv[1] == '-i':
    s.send(b'information')
    l = 0
    boof = ''
    while l == 0:
        boof = s.recv(2050).decode()
        if boof != '':
            print('Information about lamp:', boof) 
            l = 1
    exit()
        
else:
    print('ERROR: Not full information!')
    exit()

#color

if len(sys.argv) > 4 and sys.argv[3] == '-c':
    if RGB(sys.argv[4]):
        if i == 1:
            s.send(b'brightness ')
            s.send(sys.argv[2].encode() + b' ')
            s.send(b'color ')
            s.send(sys.argv[4].encode()+b' ')
        boof = ''
        l = 0
        while l == 0:
            boof = s.recv(2050).decode()
            if boof != '':
                print(boof)
                l = 1
 
    else:
        print('ERROR: Color entered incorrectly')
else:
    print('ERROR: Not full information!')
    exit()
if s:
    s.close()