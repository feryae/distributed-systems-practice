import socket

print "TCP Receiver"

print "first step: create socket"

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print "second step : bind"

ip_address = "localhost"
port_number = 50001
receiver_address = (ip_address,port_number)
s.bind(receiver_address)

print "third step: listen"

s.listen(1)

print "fourth step: accept"
print "waiting for connection...."

while True:
    conn, sender_address = s.accept()
    print "fifth step : receive data"
    data = conn.recv(1024)
    try:
        data = json.loads(datasend)
    except ValueError:
        print "bukan JSON"
    print "received", data, "from", sender_address
    print "name:", 
    conn.close()