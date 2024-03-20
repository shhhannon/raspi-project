#imports
from gpiozero import Button
from threading import Thread
import time
from gpiozero import LED

#global variables
# defgine gpio pins connected to pi
reedPin = 4
redPin = 23
greenPin = 24

reedSwitch = Button(reedPin)
redLed = LED(redPin)
greenLed = LED(greenPin)

#stores state of reed switch
switchState = None


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
            time.sleep(2)
            redLed.off()
            
        elif switchState == False:
            greenLed.on()
            
            
        time.sleep(0.1)
try:     
    switchThread = Thread(target = monitorSwitchState)
    ledThread = Thread(target = controlRGLED)

    switchThread.daemon = True
    ledThread.daemon = True

    switchThread.start()
    ledThread.start()

        
except KeyboardInterrupt:
    print("Exiting program..")
    redLed.off()
    greenLed.off()
            