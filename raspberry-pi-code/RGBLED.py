#project
import time
from colorzero import color
from gpiozero import RGBLED

#global variables
reedSwitch = True
LED = RGBLED#(redPinNum, green, blue)

#LED code
LED.color = Color('green')
while True:
    if reedSwitch == True:
        LED.color = Color('red')
        sleep(30) #Should take 30 seconds before next inhaler use
        LED.color = Color('green')
    sleep(0.1)
    
    
    