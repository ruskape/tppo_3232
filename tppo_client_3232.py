from socket import *
import sys
import json
import time 
host = 'localhost'
port = 29961
addr = (host,port)

while True:
    udp_socket = socket(AF_INET, SOCK_DGRAM)


        
    

    data = input('Please enter "info" for information or "edit" for or "control + C" for exit\n')

    match data:

        
        case '':
            udp_socket.close() 
            sys.exit(1)

        case 'info':
            #send
            data = str.encode(data)
            udp_socket.sendto(data, addr)
            data = bytes.decode(data)
            #return
            json_data, addr= udp_socket.recvfrom(1024)
            #convert string to  object
            json_object = json.loads(json_data)
            print("Speed is: ", json_object["Speed"], "Temperature is: ", json_object["Temp"],"\n")

        case 'edit':

            while True:
                Speed = input("Enter the speed value from 0 to 10\n")
                while not Speed.isnumeric():
                    print("enter a speed")
                    Speed = input("Enter again")
                Speed = int(Speed)

                Temp = input("Enter the temperature value from 15 to 35\n")
                while not Temp.isnumeric():
                    print("enter a Temperature")
                    Temp = input("Enter again")
                Temp = int(Temp)

                if (int(Temp) >= 15 and int(Temp) <= 35 and int(Speed) >= 0  and int(Speed) <= 10):
                    print("Input successs!","Temp is",Temp,"Speed is",Speed, "was set, wait notification from server")
                    json_string = json.dumps({
                    'Speed':Speed,
                    'Temp':Temp
                    })
                    data = str.encode(data)
                    udp_socket.sendto(data, addr)
                    data = bytes.decode(data)

                    json_data = str.encode(json_string)
                    udp_socket.sendto(json_data, addr)

                    time.sleep(2)
                    sucsess, addr= udp_socket.recvfrom(1024)
                    sucsess = bytes.decode(sucsess)
                    print(sucsess)
                    break
                else: 
                    print("Wrong input, please enter correct data or press " "control + C " "for exit")


                





