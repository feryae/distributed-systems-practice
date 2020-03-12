import socket
import json

print "first: create socket"

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print "no need to bind"
print "second: send data"

ip_address = "localhost"
port_number = 50000

receiver_address = (ip_address,port_number)
data = '{"Name":"Fery Ardiansyah Effendi","NIM":1301174532}'
datasend = json.dumps(data)

s.sendto(datasend,receiver_address)

print "data" , datasend , "sent to", receiver_address