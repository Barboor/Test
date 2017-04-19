import socket
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import threading


server_socket = socket.socket()
server_socket.bind(('192.168.1.22', 1111))
server_socket.listen(10)
(client_socket,  client_address) = server_socket.accept()

global k
k = 0
ClientNames = []
Details = []

def Main():
    NameCheck = client_socket.recv(1024) # from line 39 in client
    print NameCheck
    if len(ClientNames) == 0:
        ClientNames.append(NameCheck)
        print ClientNames
        print "This is ClientNames"
        client_socket.send("Ok") # to line 40 in client
    else:
        for name in ClientNames:
            if NameCheck != name:
                global k
                k = k + 1
            else:      
                pass
        if k == len(ClientNames):
            client_socket.send("Ok")
        else:
            client_socket.send("No")
            
    Info = client_socket.recv(1500) # from line 101 in client
    print Info
    print "This is 'Info'"
    ClientDetails = Info.split('\n')
    print "This is ClientDetails : " + ClientDetails
    ClientDetails.remove(ClientDetails[-1])
    Details.append(ClientDetails)

    client_socket.close()



for i in range (10):
    threading.Thread(target=Main).start()

server_socket.close()






