import paho.mqtt.client as mqtt
import time

connected = False
messageReceived = False

def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))
    if rc == 0:
        print('connected')
        global connected
        connected = True
    else: 
        print('connection failed')

def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

mqttc = mqtt.Client( 'MQTT' )
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.username_pw_set('guhpfdxf', password='jcceQ1eHsoAg')
mqttc.connect('driver.cloudmqtt.com', port=18692)
mqttc.loop_start()
mqttc.subscribe('ioioio/detected') 

while connected != True:
    time.sleep(1)
    print('hello')
while messageReceived != True:
    time.sleep(0.2)

mqttc.loop_stop()