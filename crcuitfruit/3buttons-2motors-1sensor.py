import board
import pwmio
import digitalio
import time
import adafruit_hcsr04  # Voor de ultrasone afstandssensor

# Instellen van de ultrasone sensor
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D13, echo_pin=board.D12)

# L298N Motorinstellingen voor Motor 1
IN1_M1 = digitalio.DigitalInOut(board.D3)
IN1_M1.direction = digitalio.Direction.OUTPUT

IN2_M1 = digitalio.DigitalInOut(board.D4)
IN2_M1.direction = digitalio.Direction.OUTPUT

ENA_M1 = pwmio.PWMOut(board.D5, frequency=1000)

# L298N Motorinstellingen voor Motor 2
IN1_M2 = digitalio.DigitalInOut(board.D6)
IN1_M2.direction = digitalio.Direction.OUTPUT

IN2_M2 = digitalio.DigitalInOut(board.D8)
IN2_M2.direction = digitalio.Direction.OUTPUT

ENA_M2 = pwmio.PWMOut(board.D9, frequency=1000)

# Instellen van knoppen
button1 = digitalio.DigitalInOut(board.D2)  # Voor wisselen tussen automatisch en handmatig
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.DOWN

button2 = digitalio.DigitalInOut(board.D10)  # Voor Motor 2 richting 1
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.DOWN

button3 = digitalio.DigitalInOut(board.D11)  # Voor Motor 2 richting 2
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.DOWN

# Motorbesturingsfunctie
def set_motor(motor, direction, speed):
    """
    Bestuur een motor op basis van richting en snelheid.
    :param motor: 'M1' of 'M2'
    :param direction: 'forward', 'backward', 'stop'
    :param speed: snelheid (0-65535)
    """
    if motor == "M1":
        IN1, IN2, ENA = IN1_M1, IN2_M1, ENA_M1
    elif motor == "M2":
        IN1, IN2, ENA = IN1_M2, IN2_M2, ENA_M2
    else:
        print("[FOUT] Ongeldige motor!")
        return

    if direction == "forward":
        IN1.value = True
        IN2.value = False
    elif direction == "backward":
        IN1.value = False
        IN2.value = True
    elif direction == "stop":
        IN1.value = False
        IN2.value = False
    else:
        print("[FOUT] Ongeldige richting!")
        return

    ENA.duty_cycle = speed

# Drempelwaarden
drempel_dichtbij = 5
drempel_verweg = 20
motor1_snelheid = 60768  # 50% PWM
motor2_snelheid_factor = 0.5

# Startinstellingen
is_manual = False  # Standaardmodus: automatisch
motor1_direction = "forward"
motor2_direction = "forward"

# Start de motors in "stop"
set_motor("M1", "stop", 0)
set_motor("M2", "stop", 0)

# Hoofdprogramma
print("Starten van de sensor-motor integratie...")
print("Wachten 3 seconden voordat de motoren starten...")
time.sleep(3)  # Wacht 3 seconden

try:
    while True:
        # Controleer op moduswijziging
        if button1.value:
            is_manual = not is_manual
            time.sleep(0.3)  # Debouncing
            print(f"Modus gewijzigd: {'Handmatig' if is_manual else 'Automatisch'}")

        if is_manual:
            # Handmatige modus: stuur motor 2 aan met knoppen
            if button2.value:
                set_motor("M2", "forward", int(motor1_snelheid * motor2_snelheid_factor))
            elif button3.value:
                set_motor("M2", "backward", int(motor1_snelheid * motor2_snelheid_factor))
            else:
                set_motor("M2", "stop", 0)

        else:
            # Automatische modus: gebruik de sensor om motoren aan te sturen
            try:
                afstand = sonar.distance
                print(f"Gemeten afstand: {afstand:.2f} cm")

                if afstand <= drempel_dichtbij:
                    print("Afstand dichtbij, motoren bewegen vooruit.")
                    motor1_direction = "forward"
                    motor2_direction = "forward"
                    motor1_speed = motor1_snelheid
                    motor2_speed = int(motor1_speed * motor2_snelheid_factor)
                    set_motor("M1", motor1_direction, motor1_speed)
                    set_motor("M2", motor2_direction, motor2_speed)

                elif afstand >= drempel_verweg:
                    print("Afstand ver weg, motoren bewegen achteruit.")
                    motor1_direction = "backward"
                    motor2_direction = "backward"
                    motor1_speed = motor1_snelheid
                    motor2_speed = int(motor1_speed * motor2_snelheid_factor)
                    set_motor("M1", motor1_direction, motor1_speed)
                    set_motor("M2", motor2_direction, motor2_speed)

                else:
                    print("Afstand in tussenbereik, motoren blijven in de laatste richting.")
                    set_motor("M1", motor1_direction, motor1_speed)
                    set_motor("M2", motor2_direction, motor2_speed)

            except RuntimeError:
                print("Fout bij het lezen van de sensor. Probeer opnieuw...")

        time.sleep(0.05)
except KeyboardInterrupt:
    print("Programma gestopt door gebruiker.")
    set_motor("M1", "stop", 0)
    set_motor("M2", "stop", 0)
