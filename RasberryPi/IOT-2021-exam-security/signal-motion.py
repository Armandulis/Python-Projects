import paho.mqtt.client as mqtt
from gpiozero import Button, LED

# Set up Variables with Button and LED
sensorId = 'somethin'
motionTriggered = True
motionNoticedButoonPressed = False
motionNoticedButton = Button(8)
infoLed = LED(17)

# Define button action methods
# Handles motion noticed Button let go event
def motionNoticedButtonLetGo():
    print( 'letgo')
    global motionNoticedButoonPressed
    motionNoticedButoonPressed = False

# Handles motion noticed Button pressed event
def motionNoticedButtonPressed():
    global motionNoticedButoonPressed
    if(not motionNoticedButoonPressed):
        motionNoticedButoonPressed = True
        global motionTriggered
        motionTriggered = False
            
        # Publish a message
        mqttc.publish('motion-noticed/' + sensorId, "True")

motionNoticedButton.when_pressed = motionNoticedButtonLetGo
motionNoticedButton.when_released = motionNoticedButtonPressed

# Handles new motion detected message on MQTT
def newMotionDetected():
    global motionTriggered
    motionTriggered = True
    infoLed.on()

# Handles motion handled messaged on MQTT
def motionHandled():
    global motionTriggered
    motionTriggered = False
    infoLed.off()

# Define event callbacks
# Connected to the MQTT
def on_connect(client, userdata, flags, rc):
    print('Connected!')
 
 # Received new Message
def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    newMotionDetected()
    motionHandled()

# Publish new Message
def on_publish(client, obj, mid):
    motionHandled()
 
mqttc = mqtt.Client( 'MQTT' )

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish

mqttc.username_pw_set('guhpfdxf', password='jcceQ1eHsoAg')
mqttc.connect('driver.cloudmqtt.com', port=18692)
mqttc.loop_start()

# Start subscribe, with QoS level 0
mqttc.subscribe('motion/detected')
 
# Keep listeing for new messages while the program is running
while True:
    rc = mqttc.loop()
    print( str(rc))