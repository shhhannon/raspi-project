from gpiozero import LED
from time import sleep

ledPin = 23
led = LED(ledPin)

try:
    while True:
        led.on()
        print("on")
        sleep(1)
        led.off()
        sleep(1)
        
except KeyboardInterrupt:
    led.off()
    print("off")
    