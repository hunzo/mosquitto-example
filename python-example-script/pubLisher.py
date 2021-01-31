import paho.mqtt.client as mqtt
host = "172.26.221.2"
port = 1883
client = mqtt.Client()
client.username_pw_set(username="test", password="test")
client.connect(host)
client.publish("TEST/MQTT","TEST message from publisher")