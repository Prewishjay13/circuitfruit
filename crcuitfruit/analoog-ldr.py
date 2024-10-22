import digitalio
from analogio import AnalogIn
import board
import time

analog_in = AnalogIn(board.A0)


while True:
    bitwaarde = analog_in.value
    voltage = (bitwaarde * 3.3)/65536
    print(voltage)
    time.sleep(1)