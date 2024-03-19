#imports
from gpiozero import Button, RGBLED
from threading import Thread
import time
import requests

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#global variables
# Define the GPIO pins connected to the reed switch and the RGB LED
reedPin = #add Pin NUmber
rgbLedPins = #(redPinNo, green, blue)
url = 'http://your-django-website.com/receive_data/'
doses = 200
# Initialize Button and RGBLED objects
reedSwitch = Button(reedPin)
rgbLed = RGBLED(*rgbLedPins)

# Variable to store the state of the reed switch
switchState = None
data = {'dosageTest' : str(doses)}
response = requests.post(url, data = data)

def monitorSwitchState():
    global switchState
    while True:
        if reedSwitch.is_pressed:
            switchState = "Closed"
            doses -= 1
            
        else:
            switchState = "Open"
        time.sleep(0.1)  # Small delay to avoid overheating CPU

def controlRgbLed():
    while True:
        if switchState == "Closed":
            rgbLed.color = (1, 0, 0)  # Set RGB LED to red
            time.sleep(30)  # Keep LED red for 30 seconds
            rgbLed.color = (0, 1, 0)  # Set RGB LED back to green
        else:
            rgbLed.color = (0, 1, 0)  # Set RGB LED to green
        time.sleep(0.1)  # Small delay to avoid overheating CPU

# Create threads for monitoring the switch state and controlling the RGB LED
switchThread = Thread(target=monitorSwitchState)
ledThread = Thread(target=controlRgbLed)

# Set both threads as daemon so they automatically exit when the main program exits
switchThread.daemon = True
ledThread.daemon = True

# Start both threads
switchThread.start()
ledThread.start()

try:
    while True:
        # Print the current state of the reed switch
        print("Reed switch state:", switchState)
        time.sleep(1)  # Print every second

except KeyboardInterrupt:
    print("Exiting program.")
