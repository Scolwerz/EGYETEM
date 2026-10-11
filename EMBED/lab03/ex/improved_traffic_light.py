from sense_hat import SenseHat
from time import sleep


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


def set_state():
    global state

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


state = 0
is_running = True
sense = SenseHat()

def main():
    sense.stick.direction_middle = button_event # out of order
    sense.stick.direction_down = button_event   # halt/unleash

    global state
    while True:
        if is_running:
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

            # sense.clear()
            set_state()
        else:
            pass


if __name__ == "__main__":
    main()
