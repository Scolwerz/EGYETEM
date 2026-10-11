from sense_hat import SenseHat
import time

sense = SenseHat()

state = 0
is_running = True
is_paused = False

w = (255,255,255)
r = (255,0,0)
g = (0,255,0)
y = (255,255,0)
n = (0,0,0)

red = [
    n, n, n, r, r, n, n, n,
    n, n, n, r, r, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n ]

red_yellow = [
    n, n, n, r, r, n, n, n,
    n, n, n, r, r, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, y, y, n, n, n,
    n, n, n, y, y, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n ]

yellow = [
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, y, y, n, n, n,
    n, n, n, y, y, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n ]

green = [
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, g, g, n, n, n,
    n, n, n, g, g, n, n, n ]

patterns = {
    "red": red,
    "red_yellow": red_yellow,
    "yellow": yellow,
    "green": green
}


def light_state(state_name, duration):
    pattern = patterns[state_name]
    sense.set_pixels(pattern)
    time.sleep(duration)
    sense.clear()


def out_of_order_state():
    sense.set_pixels(yellow)
    time.sleep(0.5)
    sense.clear()
    time.sleep(0.5)

def set_state():
    global state
    # state variable has been defined outside
    if state < 3:
        state += 1
    elif state == 3:
        state = 0
    else:
        pass

def button_event(event):
    global state, is_running
    if event.action == 'released':
        if event.direction == 'middle':
            if state != 4:
                state = 4
            else:
                state = 3

        if event.direction == 'down':
            is_running = not is_running


def main():
    sense.stick.direction_middle = button_event
    sense.stick.direction_down = button_event

    global state
    while True:
        if is_running:
            if state == 0:
                light_state("red", 3)
            elif state == 1:
                light_state("red_yellow", 1)
            elif state == 2:
                light_state("green", 2)
            elif state == 3:
                light_state("yellow", 1)
            else:
                out_of_order_state()
            set_state()
        else:
            sense.clear()


if __name__ == "__main__":
    main()
