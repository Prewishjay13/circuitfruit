import board
import pwmio
import time
import adafruit_hcsr04 #voor de sensor


sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D13, echo_pin=board.D12)
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
