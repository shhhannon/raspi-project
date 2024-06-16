#imports
import time
from datetime import date
from gpiozero import Button, LED
from threading import Thread
from sgp30 import SGP30
import sys
import requests
#-----------------------------------------------------------------------------------------------------------------------------

#global variables
CO2 = ""
dateAndTime = datetime.now()


# defgine gpio pins connected to pi
reedPin = 14
redPin = 24
greenPin = 23

#Iniates reedSwitch and LED objects
reedSwitch = Button(reedPin)
redLed = LED(redPin)
greenLed = LED(greenPin)

#initiates atmosphere sensor object
sgp30 = SGP30()
#stores state of reed switch
switchState = None
url = "http://127.0.0.1:8000/save_reading/"
#-----------------------------------------------------------------------------------------------------------------------------

#functions
def CO2():
    CO2 = sgp30.get_air_quality()
    dateAndTime = datetime.now() #records the date and time of inhaleruse
    data = {'CO2': CO2, 'dateTime': dateAndTime}
    requests.post(url, data=data) #sends data to django where it is then processed and added to the database

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
          
    
#main method        
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
