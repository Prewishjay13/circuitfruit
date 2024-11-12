import board
import digitalio
import pwmio
import time

# Instellingen voor de knop
button = digitalio.DigitalInOut(board.D2)  # Pas de pin aan naar waar de knop op aangesloten is
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP  # Gebruik interne pull-up weerstand

# Instellingen voor de motor (PWM)
motor_pwm = pwmio.PWMOut(board.D3, frequency=1000)  # Pin voor de motor-PWM
motor_pwm.duty_cycle = 0  # Beginstand: motor uit

# Variabele voor motorstatus
motor_on = False

# Vaste snelheid voor de motor
fixed_speed = 1500  # 50% duty cycle (0 tot 65535, dus 32768 is halve snelheid)

# Hoofdloop
while True:
    # Lees de knopstatus
    if not button.value:  # Knop ingedrukt (waarde is LOW)
        motor_on = not motor_on  # Wissel de status van de motor
        time.sleep(1)  # Debouncing tijd om te voorkomen dat het te snel schakelt

    # Stel de motor PWM in op basis van de status
    if motor_on:
        motor_pwm.duty_cycle = fixed_speed  # Stel de motor in op de vaste snelheid
        print("Motor is AAN met vaste snelheid")
    else:
        motor_pwm.duty_cycle = 0  # Zet motor uit
        print("Motor is UIT")
        
    # Korte vertraging om de loop te vertrage
    time.sleep(0.5)

