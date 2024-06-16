#imports
import os
import sys
import time
import datetime
from threading import Thread
from sgp30 import SGP30
from gpiozero import Button, LED

#set up django 
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assid.settings')
django.setup()

from assid.models import readings

#global variables
#defgine gpio pins connected to pi
reedPin = 14
redPin = 24
greenPin = 23

reedSwitch = Button(reedPin)
redLed = LED(redPin)
greenLed = LED(greenPin)

#creates the atmosphere
sgp30 = SGP30()
#stores state of reed switch
switchState = None
doses_remaining = 200

#functions
def CO2():
    CO2_reading = sgp30.get_air_quality()
    now = datetime.datetime.now() #records the date and time of inhaler use

    if switchState:
        doses_remaining -= 2 

    reading = readings.objects.create(
        CO2 = CO2_reading,
        date = now.date(),
        time = now.time(),
        doses = doses_remaining
    )
    reading.save()

def monitorSwitchState():
    while True:
        if reedSwitch.is_pressed: 
            switchState = True     #if magnetic field detected, Reed switch closes and circuit completes
            
        else:
            switchState = False
        time.sleep(0.1) # small delay to avoid overheating CPU
        
def controlRGLED():
    while True:
        if switchState == True: #if circuit complete, LED turns Red for 30 seconds
            greenLed.off()
            redLed.on()
            CO2()             #calls CO2 function
            time.sleep(30)
            redLed.off()
            
        elif switchState == False:    #circuit stays green
            greenLed.on()
        time.sleep(0.1)      # small delay to avoid overheating CPU

          
        
try:
    
    switchThread = Thread(target = monitorSwitchState)
    ledThread = Thread(target = controlRGLED)

    switchThread.daemon = False
    ledThread.daemon = False

    switchThread.start()
    ledThread.start()

   
        
except KeyboardInterrupt:
    print("Exiting program..")
    redLed.off()
    greenLed.off()
