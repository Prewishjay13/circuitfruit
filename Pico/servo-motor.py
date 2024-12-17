import time
import board
import digitalio
import pwmio
from adafruit_motor import servo

button = digitalio.DigitalInOut(board.GP5) #plek waar button gedefinieerd is
button.direction = digitalio.Direction.INPUT #button is een input
button.pull = digitalio.Pull.DOWN #spanning omlaag

#definieren van de servo motor
pwm = pwmio.PWMOut(board.GP15, duty_cycle = 2 ** 15, frequency=50)
my_servo = servo.Servo(pwm) #uitgang van de servo motor
hoek = 0 #startpunt van de motor
my_servo.angle = hoek #uitvoering van het startpunt
richting = 0 #richting aangeven

while True:
  while richting == 0: # positieve richting
    if button.value == True: #als de knop true is
      hoek += 20 #20 graden erbij
      print("+20!")
      my_servo.angle = hoek #uitvoering draaiing
      if hoek == 180: #als motor aan uiteinde is
        richting = 1 #richting veranderen
      time.sleep(0.2)
  while richting == 1: #negatieve richting
    if button.value == True: #als de knop true is
      hoek -= 20 #20 graden eraf
      print("-20")
      my_servo.angle = hoek # uitvoering draaiing
      if hoek == 0: #als motor aan het begin is
        richting = 0 #verandering richting
      time.sleep(0.2)
  else: #als er niet op de knop gedrukt word
    my_servo.angle = hoek #blijf je op dezelfde plek staan


