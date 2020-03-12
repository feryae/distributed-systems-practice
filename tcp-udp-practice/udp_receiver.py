import socket

print "socket UDP Receiver."
print "first-step:create socket"

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#AF_INET : internet is used
#SOCK_DGRAM : UDP is used


print "second step : bind "

ip_address =  "localhost"
port_number = 50000

receiver_address = (ip_address,port_number)
s.bind((receiver_address))

print "third step : receive data from "
print " waiting for something"


data, sender_address = s.recvfrom(1024)

print "received data", data
print "from ", sender_address


