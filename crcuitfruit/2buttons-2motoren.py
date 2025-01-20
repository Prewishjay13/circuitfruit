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

# Tweede motorinstellingen
IN3 = digitalio.DigitalInOut(board.D6)  # IN3 van de L298N
IN3.direction = digitalio.Direction.OUTPUT

IN4 = digitalio.DigitalInOut(board.D8)  # IN4 van de L298N (D7 vervangen door D8)
IN4.direction = digitalio.Direction.OUTPUT

ENB = pwmio.PWMOut(board.D9, frequency=1000)  # ENB (PWM-pin voor snelheid)

# Knoppen instellen
button2 = digitalio.DigitalInOut(board.D10)  # Knop 2 voor vooruit
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.DOWN

button3 = digitalio.DigitalInOut(board.D11)  # Knop 3 voor achteruit
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.DOWN

# Motorbesturingsfunctie

def set_motor(direction, speed, motor="A"):
    """
    Bestuur de motor op basis van richting en snelheid.
    :param direction: 'forward', 'backward' of 'stop'
    :param speed: snelheid (0-65535)
    :param motor: 'A' of 'B' voor de motorselectie
    """
    if motor == "A":
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
    elif motor == "B":
        if direction == "forward":
            IN3.value = True
            IN4.value = False
        elif direction == "backward":
            IN3.value = False
            IN4.value = True
        elif direction == "stop":
            IN3.value = False
            IN4.value = False

        ENB.duty_cycle = speed

    print(f"Motor {motor} ingesteld: richting = {direction}, snelheid = {speed}")

# Motor snelheid
motor_snelheid = 32768  # 50% PWM-snelheid

print("Druk op knop 2 voor vooruit, knop 3 voor achteruit.")
try:
    while True:
        if button2.value:  # Knop 2 ingedrukt
            print("Knop 2 ingedrukt, motor A vooruit, motor B achteruit.")
            set_motor("forward", motor_snelheid, motor="A")
            set_motor("backward", motor_snelheid, motor="B")
        elif button3.value:  # Knop 3 ingedrukt
            print("Knop 3 ingedrukt, motor A achteruit, motor B vooruit.")
            set_motor("backward", motor_snelheid, motor="A")
            set_motor("forward", motor_snelheid, motor="B")
        else:
            print("Geen knop ingedrukt, beide motoren stoppen.")
            set_motor("stop", 0, motor="A")
            set_motor("stop", 0, motor="B")

        time.sleep(0.1)  # Korte vertraging voor stabiliteit
except KeyboardInterrupt:
    print("Programma gestopt door gebruiker.")
    set_motor("stop", 0, motor="A")  # Stop motor A bij programma-afsluiting
    set_motor("stop", 0, motor="B")  # Stop motor B bij programma-afsluiting
