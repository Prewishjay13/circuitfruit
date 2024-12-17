import board
import digitalio
import pwmio
import time

# Debugfunctie
def debug_message(message):
    print(f"[DEBUG]: {message}")

# L298N pinconfiguratie voor Motor 1
try:
    IN1 = digitalio.DigitalInOut(board.D3)  # IN1 van L298N
    IN1.direction = digitalio.Direction.OUTPUT

    IN2 = digitalio.DigitalInOut(board.D4)  # IN2 van L298N
    IN2.direction = digitalio.Direction.OUTPUT

    ENA = pwmio.PWMOut(board.D5, frequency=1000)  # ENA (PWM-pin voor snelheid)

    debug_message("L298N pinnen correct ingesteld.")
except Exception as e:
    debug_message(f"Fout bij het instellen van de L298N-pinnen: {e}")
    raise e

# Functie om de motor te besturen
def set_motor(direction, speed):
    """
    Bestuur de motor.
    :param direction: 'forward', 'backward' of 'stop'
    :param speed: snelheid (0-65535)
    """
    if direction == "forward":
        IN1.value = True
        IN2.value = False
        debug_message("Motor draait vooruit.")
    elif direction == "backward":
        IN1.value = False
        IN2.value = True
        debug_message("Motor draait achteruit.")
    elif direction == "stop":
        IN1.value = False
        IN2.value = False
        debug_message("Motor gestopt.")
    else:
        debug_message("Ongeldige richting opgegeven!")
        return

    # Stel de snelheid in
    ENA.duty_cycle = speed
    debug_message(f"Motor snelheid ingesteld op {speed}.")

# Testloop
debug_message("Start motor test.")
try:
    while True:
        # Test: vooruit draaien
        debug_message("Test: Motor vooruit op 50% snelheid.")
        set_motor("forward", 32768)  # 50% snelheid vooruit
        time.sleep(2)

        # Test: achteruit draaien
        debug_message("Test: Motor achteruit op 50% snelheid.")
        set_motor("backward", 32768)  # 50% snelheid achteruit
        time.sleep(2)

        # Test: motor stoppen
        debug_message("Test: Motor stoppen.")
        set_motor("stop", 0)  # Stop de motor
        time.sleep(2)
except KeyboardInterrupt:
    debug_message("Test gestopt door gebruiker.")
    set_motor("stop", 0)  # Zorg dat de motor stopt bij exit
except Exception as e:
    debug_message(f"Fout in hoofdloop: {e}")
    raise e
