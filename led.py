from gpiozero import LED
from time import sleep

led = LED(17)  # Replace with your GPIO pin number

try:
    while True:
        led.on()
        sleep(0.5)
        led.off()
        sleep(0.5)
except KeyboardInterrupt:
    print("Script interrupted. Cleaning up...")
    led.off()  # Turn off the LED before exiting
