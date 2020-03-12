import paho.mqtt.client as mqtt

broker_ip="192.168.43.17"
topic="/two/humidity"


def on_connect(client, userdata, flags, rc):
    print("Connect "+str(rc))
    client.subscribe("#")

def on_message(client, userdata, msg):
    print(str(msg.payload))

client=mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message

client.connect(broker_ip)

client.loop_forever()