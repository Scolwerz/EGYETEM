# Imports and the SenseHat object
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

# Create a variable which keeps track the state of your state machine
state = 0

# Define colors to the light representation
w = (255,255,255)
r = (255,0,0)
g = (0,255,0)
y = (255,255,0)
n = (0,0,0)

# Predefined patters to the states
red = [n, n, n, r, r, n, n, n,
    n, n, n, r, r, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n]

red_yellow = [n, n, n, r, r, n, n, n,
    n, n, n, r, r, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, y, y, n, n, n,
    n, n, n, y, y, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n]

yellow = [n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, y, y, n, n, n,
    n, n, n, y, y, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n]

green = [n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, g, g, n, n, n,
    n, n, n, g, g, n, n, n]

def set_state():
    global state
    # state variable has been defined outside
    if state < 3:
        state += 1
    elif state == 3:
        state = 0
    else:
        pass

# Create an event handler to the joystick button. At the first press of the
# button, the state machine goes into the out of order mode (state == 4)
# while the next press turns back the state machine into normal mode
def button_event(event):
    global state
    if event.action == 'released':
        if state != 4:
            state = 4
        else:
            state = 3

# Define joystick's trigger event
sense.stick.direction_middle = button_event

# The main function is a state machine which is running in an infinite loop.
# The last state is an 'out of order state'.
def main():
    global state
    while True:
        if state == 0:
            sense.set_pixels(red)
            sleep(3)
        elif state == 1:
            sense.set_pixels(red_yellow)
            sleep(1)
        elif state == 2:
            sense.set_pixels(green)
            sleep(2)
        elif state == 3:
            sense.set_pixels(yellow)
            sleep(1)
        else:
            sense.set_pixels(yellow)
            sleep(0.5)
            sense.clear()
            sleep(0.5)
        sense.clear()
        set_state()

if __name__ == "__main__":
    main()
