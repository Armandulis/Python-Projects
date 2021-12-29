import requests
from datetime import datetime

payload = { 'sensorId': 33333, 'measurementTime': datetime.now() }
r = requests.put( 'http://localhost:3000/motion', payload )

print( r.text ) 


r = requests.get( 'http://localhost:3000/motion?sensorId=22132' )
print( r.text )


r = requests.get( 'http://localhost:3000/motion/latest' )
print( r.text )

from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(23, 24)

while True:
    print('Distance to nearest object is', sensor.distance, 'm')
    sleep(1)