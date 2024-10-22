import digitalio
import board
import time

led = digitalio.DigitalInOut(board.LED)
#led = digitalio.DigitalInOut(board.D10) # GP10 voor Pi Pic
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(3)
    led.value = False
    time.sleep(1)
    

