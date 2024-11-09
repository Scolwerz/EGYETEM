from sense_hat import SenseHat
import time

sense = SenseHat()

delay_val = 1.0

w = (255,255,255)
n = (0,0,0)

on = [
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w ]

off = [
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n ]


def delay(event):
    global delay_val
    # delay_val is a global variable because it has been defined outside of this function
    print(event.direction)
    if event.action == 'pressed':
        if event.direction == "middle":
            delay_val = 0.2
        elif event.direction == "up":
            delay_val = 0.1
        elif event.direction == "down":
            delay_val = 2.0
        elif event.direction == "left":
            delay_val = 1.5
        elif event.direction == "right":
            delay_val = 0.5
    elif event.action == 'released':
        delay_val = 1.0


def main():
    sense.stick.direction_middle = delay
    sense.stick.direction_up = delay
    sense.stick.direction_down = delay
    sense.stick.direction_left = delay
    sense.stick.direction_right = delay

    while True:
        sense.set_pixels(on)
        time.sleep(delay_val)
        sense.set_pixels(off)
        time.sleep(delay_val)



if __name__ == "__main__":
    main()
