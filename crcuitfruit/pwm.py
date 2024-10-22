import timeimport board
import pwmio
pwm_led = pwmio.PWMOut(board.D13)

while True:
    for cycle in range(65535):
        pwm_led.duty_cycle = cycle
    for cycle in range(65535, 0, -1):
        pwm_led.duty_cycle = cycle
        
