#imports
from gpiozero import Button
from threading import Thread
import time
from gpiozero import LED
from sgp30 import SGP30
import sys

#global variables
# defgine gpio pins connected to pi
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

def crude_progress_bar():
    sys.stdout.write('.')
    sys.stdout.flush()
def CO2():
    result = sgp30.get_air_quality()
    print(result)
def monitorSwitchState():
    global switchState
    while True:
        if reedSwitch.is_pressed:
            switchState = True
            
        else:
            switchState = False
        
        time.sleep(0.1) # small delay to avoid overheating CPU
        
def controlRGLED():
    while True:
        if switchState == True:
            greenLed.off()
            redLed.on()
            CO2()
            time.sleep(30)
            redLed.off()
            
        elif switchState == False:
            greenLed.on()
        time.sleep(0.1)
          

            
        
try:
    
    
    #CO2Thread = Thread(target = CO2)
    switchThread = Thread(target = monitorSwitchState)
    ledThread = Thread(target = controlRGLED)

    switchThread.daemon = False
    ledThread.daemon = False
    #CO2Thread.daemon = True

    switchThread.start()
    ledThread.start()
    #CO2Thread.start()
    sgp30.start_measurement(crude_progress_bar)
    sys.stdout.write('\n')
        
except KeyboardInterrupt:
    print("Exiting program..")
    redLed.off()
    greenLed.off()