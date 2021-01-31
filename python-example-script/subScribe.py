import paho.mqtt.client as mqtt
host = "172.26.221.2"
port = 1883

def on_connect(self, client, userdata, rc):
    print("MQTT Connected.")
    self.subscribe("TEST/MQTT")

def on_message(client, userdata,msg):
    test = msg.payload.decode("utf-8", "strict")
    print(type(test))
    print(test)


client = mqtt.Client()
client.username_pw_set(username="test", password="test")
client.on_connect = on_connect
client.on_message = on_message
client.connect(host)
client.loop_forever()

