from sense_hat import SenseHat
import time
import random

sense = SenseHat()

b = (0, 0, 255)
n = (0, 0, 0)

def shift_down():
    for y in range(7, 0, -1):
        for x in range(8):
            sense.set_pixel(x, y, sense.get_pixel(x, y - 1))

    for x in range(8):
        sense.set_pixel(x, 0, n)


def main():
    while True:
        sense.set_pixel(random.randint(0, 7), 0, b)
        time.sleep(0.5)
        shift_down()

if __name__ == "__main__":
    main()
