# tppo_3232
A smart fan is software designed to control the speed and temperature of a device. It is designed based on Python. This application has 2 sides: server and client.

---

## Table of contents

1.  [ Overview ](#overview)
2.  [ Dependencies ](#dependencies)
3.  [ Installation ](#installation)
4.  [ Run ](#run)
5.  [ Support ](#support)


---

<a name="overview"></a>
## 1. Overview

This app has 2 sides: server and client. 
A service chat monitor changes in the state of a smart fan, simulated by a local file, and receive / transmit requests and responses via a network control protocol.
A client program for managing the device through the service (and checking the operation of the service).

---

<a name="dependencies"></a>
## 2. Dependencies

- [Python (>=3.7)](https://www.python.org/)
- time
- sys
- socket
- json

---

<a name="installation"></a>
## 3. Installation

Steps:

1. git clone https://github.com/ruskape/tppo_3232.git or download ZIP
2. cd tppo_3232

---

<a name="run"></a>
## 4. Run
1. Make the files executable
```
chmod +x tppo_client_3232.py
chmod +x tppo_server_3232.py
```
2. Start the service
```
./tppo_server_3232.py
```
3. Start the client file with the  key words:

    3.1. ```info``` is a key for getting information about fan state.
    
    3.2. ```-edit```, is a key for setting the speed and temperature of the fan. 
      
      Speed - glow intensity (0 .. 10 conditional units). 
      
      Fan - glow intensity (15 .. 35 °C). 


<a name="support"></a>
## 5. Support

- Email at - ruskapecontact@gmail.com.

---

