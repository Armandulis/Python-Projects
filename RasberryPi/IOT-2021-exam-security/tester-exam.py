import requests
from datetime import datetime
from time import sleep
# from gpiozero import DistanceSensor
# from picamera import PiCamera
import base64

# payload = { 'sensorId': 33333, 'measurementTime': datetime.now() }
# r = requests.put( 'http://localhost:3000/motion', payload )

# print( r.text ) 


# r = requests.get( 'http://localhost:3000/motion?sensorId=22132' )
# print( r.text )


# r = requests.get( 'http://localhost:3000/motion/latest' )
# print( r.text )

# camera = PiCamera()
# sensor = DistanceSensor(23, 24 )


with open('./CerealsBank.png', 'rb') as image_file:
    encoded_string = base64.b64encode(image_file.read())

payload = { 'sensorId': 'ioioio', 'measurementTime': datetime.now(), 'base64Picture':  encoded_string }
r = requests.post( 'https://iot-2021-security-api.herokuapp.com/motion', payload)
print( r.text )

# def motionDetected():
#     currentTime = datetime.now().strftime('%y-%m-%d')
#     filePath = f'/home/pi/Desktop/captured-pictures/{currentTime}.jpeg'
#     camera.capture( filePath )
# with open('/home/pi/Desktop/captured-pictures/waqe.jpeg', 'rb') as image_file:
#     encoded_string = base64.b64encode(image_file.read())

