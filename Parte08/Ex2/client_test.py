#!/usr/bin/env python3
# --------------------------------------------------
# Fábio Sousa.
# PSR, November 2022.
# --------------------------------------------------
import socket
import time
import dog_lib

dog = dog_lib.Dog(name='Toby', age=7, color='brown')  # instantiate a new dog
dog.addBrother('Lassie')
dog.addBrother('Bobby')
print('CLIENT: my dog has ' + str(dog))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create TCP/IP socket
local_hostname = socket.gethostname()  # retrieve local hostname
local_fqdn = socket.getfqdn()  # get fully qualified hostname
ip_address = socket.gethostbyname(local_hostname)  # get the according IP address

server_address = (ip_address, 23456)  # bind the socket to the port 23456, and connect
sock.connect(server_address)
print ("connecting to %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))

# define example data to be sent to the server
# messages = ([30, 'Robotics', 31, 14, 'Automation', 18])
# for message in messages:
#     message = str(message).encode()
#     print ('Sending message: ' + str(message))
#     sock.sendall(message) #Converts message to string and then to bytes in ascii encoding
#     time.sleep(2)  # wait for two seconds

sock.sendall(str(dog).encode()) #Converts message to string and then to bytes in ascii encoding
print ('Sending message: ' + str(dog))
    
sock.close()  # close connection