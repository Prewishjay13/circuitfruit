import board
import pwmio
import digitalio
import time
import adafruit_hcsr04  # Voor de ultrasone afstandssensor

# Instellen van de ultrasone sensor
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D13, echo_pin=board.D12)

# L298N Motorinstellingen
IN1 = digitalio.DigitalInOut(board.D3)  # IN1 van de L298N
IN1.direction = digitalio.Direction.OUTPUT

IN2 = digitalio.DigitalInOut(board.D4)  # IN2 van de L298N
IN2.direction = digitalio.Direction.OUTPUT

ENA = pwmio.PWMOut(board.D5, frequency=1000)  # ENA (PWM-pin voor snelheid)

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
    else:
        print("Ongeldige richting opgegeven!")
        return

    ENA.duty_cycle = speed
    print(f"Motor ingesteld: richting = {direction}, snelheid = {speed}")

# Drempelwaarden
drempel_dichtbij = 5  # Sensorwaarde 5 cm of minder
drempel_verweg = 20  # Sensorwaarde 20 cm of meer
motor_snelheid = 32768  # 50% PWM-snelheid

# Hoofdprogramma
print("Starten van de sensor-motor integratie...")
try:
    while True:
        try:
            afstand = sonar.distance  # Lees de afstand
            print(f"Gemeten afstand: {afstand:.2f} cm")

            if afstand <= drempel_dichtbij:
                print("Afstand dichtbij, motor beweegt vooruit.")
                set_motor("forward", motor_snelheid)
            elif afstand >= drempel_verweg:
                print("Afstand ver weg, motor beweegt achteruit.")
                set_motor("backward", motor_snelheid)
            #deze gedeelte moest weg anderst werkt de code buiten de drempels
            # else:
            #     print("Afstand binnen neutrale zone, motor stopt.")
            #     set_motor("stop", 0)

        except RuntimeError:
            print("Fout bij het lezen van de sensor. Probeer opnieuw...")
        
        time.sleep(0.1)  # Korte vertraging voor stabiliteit
except KeyboardInterrupt:
    print("Programma gestopt door gebruiker.")
    set_motor("stop", 0)  # Motor uitzetten bij stoppen

