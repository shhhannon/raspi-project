#Reed Switch
from gpiozero import Button
import time

REEDPIN = #GPIO pin

# Initialize a Button object for the reed switch
reedSwitch = Button(REED_PIN)

# Variable to store the state of the reed switch
switch_state = None

try:
    while True:
        # Check if the reed switch is closed (magnet near)
        if reed_switch.is_pressed:
            switch_state = "Closed"
        else:
            switch_state = "Open"
        
        # Print the current state of the reed switch
        print("Reed switch state:", switch_state)
        
        # Add a small delay to avoid high CPU usage
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nExiting program.")
