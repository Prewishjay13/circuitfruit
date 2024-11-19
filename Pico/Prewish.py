import time
import board
import digitalio

# Set up the red LED
red_led = digitalio.DigitalInOut(board.GP9)
red_led.direction = digitalio.Direction.OUTPUT

# Set up the green LED
green_led = digitalio.DigitalInOut(board.GP5)
green_led.direction = digitalio.Direction.OUTPUT

# Set up the button
button = digitalio.DigitalInOut(board.GP7)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN  # Ensures a default state for the button

#Set up the blink delay, button state and the current led that is on or that will be on when code runs
blink_delay = 2  # Initial delay for blinking
previous_button_state = False
current_led = "red"  # Start with the red LED active

# Main loop
while True:
    # Toggle LEDs based on the current 
    if current_led == "red":
        red_led.value = True
        green_led.value = False
    else:
        red_led.value = False
        green_led.value = True

    time.sleep(blink_delay)

    # Switch to the other LED
    current_led = "green" if current_led == "red" else "red"

    # Check if the button is being pressed
    current_button_state = button.value
    if current_button_state and not previous_button_state:  # Button just pressed
        print("Button Pressed!")

        # Keep the currently active LED on for 1 secondwhen button is pressed
        if current_led == "red":
            green_led.value = False
            red_led.value = True
            time.sleep(1)
        elif current_led == "green":
            red_led.value = False
            green_led.value = True
            time.sleep(1)

        # Speed up blinking by reducing the delay
        blink_delay = max(0.1, blink_delay - 0.01)  # Minimum delay is 0.1 seconds
        print(f"New Blink Delay: {blink_delay} seconds")

    # Update previous button state
    previous_button_state = current_button_state
    time.sleep(0.1)
