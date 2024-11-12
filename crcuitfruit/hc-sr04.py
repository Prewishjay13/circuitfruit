import time
import board
import digitalio

# Define pins
trigger_pin = board.D2
echo_pin = board.D3

# Set up trigger and echo as digital pins
trigger = digitalio.DigitalInOut(trigger_pin)
trigger.direction = digitalio.Direction.OUTPUT
echo = digitalio.DigitalInOut(echo_pin)
echo.direction = digitalio.Direction.INPUT

def measure_distance():
    # Send a 10us pulse to trigger the measurement
    trigger.value = True
    time.sleep(0.00001)  # 10 microseconds
    trigger.value = False

    # Wait for the echo to go high, then start timing
    while not echo.value:
        pass
    start_time = time.monotonic()

    # Wait for the echo to go low, then record the end time
    while echo.value:
        pass
    end_time = time.monotonic()

    # Calculate distance (in centimeters)
    duration = end_time - start_time
    distance_cm = (duration * 34300) / 2  # Speed of sound is 34300 cm/s

    return distance_cm

while True:
    distance = measure_distance()
    print("Distance:", distance, "cm")
    time.sleep(1)
