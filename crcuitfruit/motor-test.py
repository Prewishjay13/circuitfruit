import board
import digitalio
import pwmio
import time

IN1 = digitalio.DigitalInOut(board.D3)  # IN1 van L298N
IN1.direction = digitalio.Direction.OUTPUT

IN2 = digitalio.DigitalInOut(board.D4)  # IN2 van L298N
IN2.direction = digitalio.Direction.OUTPUT

def motor_forward(speed):
    IN1.value = True
    IN2.value = False
    ENA.duty_cycle = int(speed * 65535 / 100)
    
while True:
    motor_forward(100)
    time.sleep(1)

