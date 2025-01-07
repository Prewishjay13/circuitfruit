import board
import pwmio
import digitalio
import time
import adafruit_hcsr04  # Voor de ultrasone afstandssensor

# Instellen van de ultrasone sensor
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D13, echo_pin=board.D12)

# L298N Motorinstellingen voor Motor 1
IN1_M1 = digitalio.DigitalInOut(board.D3)  # IN1 van de L298N voor Motor 1
IN1_M1.direction = digitalio.Direction.OUTPUT

IN2_M1 = digitalio.DigitalInOut(board.D4)  # IN2 van de L298N voor Motor 1
IN2_M1.direction = digitalio.Direction.OUTPUT

ENA_M1 = pwmio.PWMOut(board.D5, frequency=1000)  # ENA (PWM-pin voor snelheid van Motor 1)

# L298N Motorinstellingen voor Motor 2
IN1_M2 = digitalio.DigitalInOut(board.D6)  # IN1 van de L298N voor Motor 2
IN1_M2.direction = digitalio.Direction.OUTPUT

IN2_M2 = digitalio.DigitalInOut(board.D7)  # IN2 van de L298N voor Motor 2
IN2_M2.direction = digitalio.Direction.OUTPUT

ENA_M2 = pwmio.PWMOut(board.D8, frequency=1000)  # ENA (PWM-pin voor snelheid van Motor 2)

# Huidige status van de motoren
current_direction = "stop"

# Motorbesturingsfunctie
def set_motor(motor, direction, speed):
    """
    Bestuur een motor op basis van richting en snelheid.
    :param motor: 'M1' of 'M2' om aan te geven welke motor wordt bestuurd.
    :param direction: 'forward', 'backward' of 'stop'
    :param speed: snelheid (0-65535)
    """
    global current_direction

    if motor == "M1":
        IN1, IN2, ENA = IN1_M1, IN2_M1, ENA_M1
    elif motor == "M2":
        IN1, IN2, ENA = IN1_M2, IN2_M2, ENA_M2
    else:
        print("Ongeldige motor opgegeven!")
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
        print("Ongeldige richting opgegeven!")
        return

    ENA.duty_cycle = speed
    if motor == "M1":
        current_direction = direction
    print(f"Motor {motor} ingesteld: richting = {direction}, snelheid = {speed}")

# Drempelwaarden
drempel_dichtbij = 5  # Sensorwaarde 5 cm of minder
drempel_verweg = 20  # Sensorwaarde 20 cm of meer
motor1_snelheid = 32768  # 50% PWM-snelheid voor Motor 1
motor2_snelheid_factor = 0.25  # Motor 2 draait op een vierde van de snelheid van Motor 1

# Hoofdprogramma
print("Starten van de sensor-motor integratie...")
try:
    while True:
        try:
            afstand = sonar.distance  # Lees de afstand
            print(f"Gemeten afstand: {afstand:.2f} cm")

            if afstand <= drempel_dichtbij:
                print("Afstand dichtbij, motoren bewegen vooruit.")
                motor1_speed = motor1_snelheid
                motor2_speed = int(motor1_speed * motor2_snelheid_factor)
                set_motor("M1", "forward", motor1_speed)
                set_motor("M2", "forward", motor2_speed)
            elif afstand >= drempel_verweg:
                print("Afstand ver weg, motoren bewegen achteruit.")
                motor1_speed = motor1_snelheid
                motor2_speed = int(motor1_speed * motor2_snelheid_factor)
                set_motor("M1", "backward", motor1_speed)
                set_motor("M2", "backward", motor2_speed)
            else:
                print("Afstand binnen neutrale zone, motoren stoppen.")
                set_motor("M1", "stop", 0)
                set_motor("M2", "stop", 0)

        except RuntimeError:
            print("Fout bij het lezen van de sensor. Probeer opnieuw...")

        time.sleep(0.1)  # Korte vertraging voor stabiliteit
except KeyboardInterrupt:
    print("Programma gestopt door gebruiker.")
    set_motor("M1", "stop", 0)  # Motor 1 uitzetten bij stoppen
    set_motor("M2", "stop", 0)  # Motor 2 uitzetten bij stoppen
