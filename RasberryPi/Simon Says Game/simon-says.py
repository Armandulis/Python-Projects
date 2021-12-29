# External module imports
import RPi.GPIO as GPIO
import time
import random

# Pin Definitons:
greenLed = 18 # Broadcom pin 18 
redLed = 23 # Broadcom pin 23 
blueLed = 25 # Broadcom pin 25

greenButtonPin = 17 # Broadcom pin 17 
redButtonPin = 5 # Broadcom pin 5
blueButtonPin = 13 # Broadcom pin 13

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setwarnings(False)

GPIO.setup(greenLed, GPIO.OUT) # LED pin set as output
GPIO.setup(redLed, GPIO.OUT) # LED pin set as output
GPIO.setup(blueLed, GPIO.OUT) # LED pin set as output

GPIO.setup(greenButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(redButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(blueButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

level = 1
pattern = []
userPatter = []
colors = { 'Green': 0, 'Red': 1, 'Blue': 2 }

print( 'Here we go! Press CTRL+C to exit' )
print( f'Level: {level}' ) 

# Turn on green led and turn off the others
def lightUpGreen():
    GPIO.output(greenLed, GPIO.HIGH)
    GPIO.output(redLed, GPIO.LOW)
    GPIO.output(blueLed, GPIO.LOW)

# Turn on red led and turn off the others
def lightUpRed():
    GPIO.output(greenLed, GPIO.LOW)
    GPIO.output(redLed, GPIO.HIGH)
    GPIO.output(blueLed, GPIO.LOW)

# Turn on blue led and turn off the others    
def lightUpBlue():
    GPIO.output(greenLed, GPIO.LOW)
    GPIO.output(redLed, GPIO.LOW)
    GPIO.output(blueLed, GPIO.HIGH)

# Turn off all lights
def turnOffLights():
    GPIO.output(greenLed, GPIO.LOW)
    GPIO.output(redLed, GPIO.LOW)
    GPIO.output(blueLed, GPIO.LOW)

# Turn on all lights
def turnOnLights():
    GPIO.output(greenLed, GPIO.HIGH)
    GPIO.output(redLed, GPIO.HIGH)
    GPIO.output(blueLed, GPIO.HIGH)


# Start level
def startLevel():

    # Shine lights for a bit to sigal that the level is about to start
    turnOnLights()
    time.sleep(0.2)
    turnOffLights()
    time.sleep(0.2)
    turnOnLights()
    time.sleep(0.2)
    turnOffLights()
    time.sleep(0.5)

    # Add random color to the pattern
    colorNumber = random.randint(0, 2)
    pattern.append( colorNumber )
    for color in pattern:
        if color == colors['Green']:
            lightUpGreen()
            time.sleep(0.5)
        if color == colors['Red']:
            lightUpRed()
            time.sleep(0.5)
        if color == colors['Blue']:
            lightUpBlue()
            time.sleep(0.5)
        turnOffLights()    
        time.sleep(0.1)


# Get users input and shine led upon press
def getUsersInput():
    buttonPressed = False
    while 1:
        # Add pressed color to the pattern after user clicked the button
        if not GPIO.input(greenButtonPin): # button is pressed
            GPIO.output(greenLed, GPIO.HIGH)
            if not buttonPressed:
                userPatter.append( 0 )
                buttonPressed = True
        else: # button is realsed:
            GPIO.output(greenLed, GPIO.LOW)
            if buttonPressed:
                break

        if not GPIO.input(redButtonPin): # button is pressed
            GPIO.output(redLed, GPIO.HIGH)
            if not buttonPressed:
                userPatter.append( 1 )
                buttonPressed = True
        else: # button is realsed:
            GPIO.output(redLed, GPIO.LOW)
            if buttonPressed:
                break

        if not GPIO.input(blueButtonPin): # button is pressed
            GPIO.output(blueLed, GPIO.HIGH)
            if not buttonPressed:
                userPatter.append( 2 )
                buttonPressed = True
        else: # button is realsed:
            GPIO.output(blueLed, GPIO.LOW)
            if buttonPressed:
                break


# Play the game 
try:
    while True:
        
        startLevel()
        # Wait for user to provide the pattern
        while len(pattern) != len(userPatter):
            getUsersInput()
            time.sleep(0.5)
        
        time.sleep(0.2)
        turnOffLights()

        # Check if users pattern matches levels pattern
        if userPatter != pattern:
            print( f'You lost! You reached level {level}!' )
            for num in range(10):
                lightUpRed()
                time.sleep( 0.2 )
                turnOffLights()
                time.sleep(0.2)
            userPatter = []
            pattern = []
            level = 1
        else:
            level = level + 1
            print( f'Level: {level}')
            userPatter = []
            
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
