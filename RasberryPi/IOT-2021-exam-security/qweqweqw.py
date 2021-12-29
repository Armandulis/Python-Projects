import requests
from datetime import datetime
import base64

# payload = { 'sensorId': 33333, 'measurementTime': datetime.now() }
# r = requests.put( 'http://localhost:3000/motion', payload )

# print( r.text ) 


# r = requests.get( 'http://localhost:3000/motion?sensorId=22132' )
# print( r.text )


# r = requests.get( 'http://localhost:3000/motion/latest' )
# print( r.text )

from gpiozero import DistanceSensor
from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution( 1280, 720 )
camera = PiCamera()
filePath = ''

def motionDetected():
    currentTime = datetime.now()
    filePath = f'/home/pi/Desktop/captured-pictures/{currentTime}.jpeg'
    camera.capture( filePath )
    # camera.capture(f'/Desktop/captured-pictures/{datetime.now().strftime("%d/%m/%y")}.jpeg')

sensor = DistanceSensor(23, 24 )

while True:
    if sensor.distance < 0.5:
        motionDetected()
        with open(filePath, 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read())

        payload = { 'sensorId': 'ioioio', 'measurementTime': datetime.now(), 'base64Picture':  encoded_string }
        r = requests.post( 'http://localhost:3000/motion', payload)
        print( r.text )




       
