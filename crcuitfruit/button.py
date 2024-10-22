import digitalio
import board

led = digitalio.DigitalInOut(board.D10)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
#of
#button.pull = digitalio.Pull.DOWN

while True:
    if button.value:
        led.value = False
    else:
        led.value = True
        
    