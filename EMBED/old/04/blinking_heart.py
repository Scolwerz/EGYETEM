from sense_hat import SenseHat
import time

sense = SenseHat()

o = (0, 0, 0)     # black
r = (255, 0, 0)   # red

heart_pixels = [
    o, o, o, o, o, o, o, o,
    o, r, r, o, o, r, r, o,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    o, r, r, r, r, r, r, o,
    o, o, r, r, r, r, o, o,
    o, o, o, r, r, o, o, o,
    o, o, o, o, o, o, o, o]


def blink_heart():
    for _ in range(5):
        sense.set_pixels(heart_pixels)
        time.sleep(0.5)
        sense.clear()
        time.sleep(0.5)

def red():
    sense.clear(255, 0, 0)

def blue():
    sense.clear(0, 0, 255)

def green():
    sense.clear(0, 255, 0)

def yellow():
    sense.clear(255, 255, 0)


def main():
    sense.stick.direction_up = blink_heart
    sense.stick.direction_down = blue
    sense.stick.direction_left = green
    sense.stick.direction_right = yellow
    sense.stick.direction_middle = sense.clear

    while True:
        pass



if __name__ == "__main__":
    main()
