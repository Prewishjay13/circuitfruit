import board
import pwmio
import digitalio
import time

# L298N Motorinstellingen
IN1 = digitalio.DigitalInOut(board.D3)  # IN1 van de L298N
IN1.direction = digitalio.Direction.OUTPUT

IN2 = digitalio.DigitalInOut(board.D4)  # IN2 van de L298N
IN2.direction = digitalio.Direction.OUTPUT

ENA = pwmio.PWMOut(board.D5, frequency=1000)  # ENA (PWM-pin voor snelheid)

# Knoppen instellen
button2 = digitalio.DigitalInOut(board.D10)  # Knop 2 voor vooruit
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.DOWN

button3 = digitalio.DigitalInOut(board.D11)  # Knop 3 voor achteruit
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.DOWN

# Motorbesturingsfunctie
def set_motor(direction, speed):
    """
    Bestuur de motor op basis van richting en snelheid.
    :param direction: 'forward', 'backward' of 'stop'
    :param speed: snelheid (0-65535)
    """
    if direction == "forward":
        IN1.value = True
        IN2.value = False
    elif direction == "backward":
        IN1.value = False
        IN2.value = True
    elif direction == "stop":
        IN1.value = False
        IN2.value = False

    ENA.duty_cycle = speed
    print(f"Motor ingesteld: richting = {direction}, snelheid = {speed}")

# Motor snelheid
motor_snelheid = 32768  # 50% PWM-snelheid

print("Druk op knop 2 voor vooruit, knop 3 voor achteruit.")
try:
    while True:
        if button2.value:  # Knop 2 ingedrukt
            print("Knop 2 ingedrukt, motor beweegt vooruit.")
            set_motor("forward", motor_snelheid)
        elif button3.value:  # Knop 3 ingedrukt
            print("Knop 3 ingedrukt, motor beweegt achteruit.")
            set_motor("backward", motor_snelheid)
        else:
            print("Geen knop ingedrukt, motor stopt.")
            set_motor("stop", 0)

        time.sleep(0.1)  # Korte vertraging voor stabiliteit
except KeyboardInterrupt:
    print("Programma gestopt door gebruiker.")
    set_motor("stop", 0)  # Stop motor bij programma-afsluiting
