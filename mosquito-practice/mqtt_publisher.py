import paho.mqtt.client as mqtt

broker_ip = "192.168.43.17"
#topic = "/one/temperature"
topic = "/two/humidity"

i = 0
for i in range(10): 
    i = i+1
    j = str(i)
    message = " "+j

    #first step : create client

    client = mqtt.Client("P1")

    #second step : connect to broker

    client.connect(broker_ip)

    #third step : publish

    client.publish(topic,message)
