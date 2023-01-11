from socket import *
import json
import sys

#top
host = 'localhost'
port = 29961
addr = (host,port)
udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(addr)
Speed = 5
Temp = 25
L = [Speed, Temp]


# Запись 
f = open('cfg.bin', 'wb')
for item in L:
    st = str(item) + '\n'
    bt = st.encode()
    f.write(bt) 
f.close();

# Считать список 
L2 = []
f = open('cfg.bin', 'rb')
for ln in f:
    x = int(ln) 
    L2 = L2 + [x]    
print("Speed = ", L2[0], ' ', "Temp = ", L2[1],"\n") 
f.close();

users = []

#Cycle
while True:
    print('Wait command...')

    data, addr = udp_socket.recvfrom(1024)

    users.append(addr)

    print('Client addr: ', addr)
    print('msg: ', data)

    data = bytes.decode(data)
    match data:
         case '':
            udp_socket.close() 
            sys.exit(1)

         case 'info':
            print("Client check status","\n")
            # Считать список из бинарного файла 
            L2 = []
            f = open('cfg.bin', 'rb')
            for ln in f:
               x = int(ln) 
               L2 = L2 + [x] 
            f.close();

            # Send L2 as JSON 
            json_string = json.dumps({
                  'Speed':Speed,
                  'Temp':Temp
            })
            print(json_string,"\n")
            json_data = str.encode(json_string)
            udp_socket.sendto(json_data, addr)

         case 'edit':
            print("Client check editing parameters","\n")
            #get json
            json_data, addr= udp_socket.recvfrom(1024)
            #convert string to  object
            json_object = json.loads(json_data)
            print("JSON - Speed is: ", json_object["Speed"], "Temperature is: ", json_object["Temp"],"\n")
            
            # Запись файла
            Speed = int(json_object["Speed"])
            Temp = int(json_object["Temp"])

            # Write
            L3 = [Speed, Temp]
            f = open('cfg.bin', 'wb')
            for item in L3:
               st = str(item) + '\n'
               bt = st.encode()
               f.write(bt) 
            f.close();

            # check
            L4 = []
            f = open('cfg.bin', 'rb')
            for ln in f:
               x = int(ln) 
               L4 = L4 + [x] 

            if L3[0] == L4[0] and L3[1] == L4[1]:
               print("Speed = ", L4[0], ' ', "Temp = ", L4[1],"\n") 
               sucsess = "Parameters was editing - Speed = ", L4[0], " Temp = ", L4[1], "\n"
               sucsess = str(sucsess)
               sucsess = str.encode(sucsess)
               udp_socket.sendto(sucsess, addr)




















      

  
