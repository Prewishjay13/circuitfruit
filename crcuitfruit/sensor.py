import board
import pwmio
import time
import adafruit_hcsr04 #voor de sensor
##sensor aan 5v aansluiten!

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP3, echo_pin=board.GP4)
drempel = 5

while True:
    try:
        afstand = sonar.distance
        if afstand <= drempel:
            print("sensor aan")
        else:
            print("sensor uit")
        print(afstand)
    except RuntimeError:
        print("retrying")
    time.sleep(0.005)