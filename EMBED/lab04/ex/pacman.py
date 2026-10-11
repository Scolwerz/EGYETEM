from sense_hat import SenseHat
from time import sleep

y = (255, 255, 0)
b = (0, 0, 255)
o = (0, 0, 0)

pacman1 = [
    o, y, y, y, y, y, o, o,
    y, y, y, y, y, o, o, o,
    y, y, y, y, o, o, o, o,
    y, y, y, o, o, o, b, b,
    y, y, y, o, o, o, b, b,
    y, y, y, y, o, o, o, o,
    y, y, y, y, y, o, o, o,
    o, y, y, y, y, y, o, o
]

pacman2 = [
    o, y, y, y, y, y, o, o,
    y, y, y, y, y, y, o, o,
    y, y, y, y, y, o, o, o,
    y, y, y, y, o, b, b, o,
    y, y, y, y, o, b, b, o,
    y, y, y, y, y, o, o, o,
    y, y, y, y, y, y, o, o,
    o, y, y, y, y, y, o, o
]

pacman3 = [
    o, y, y, y, y, y, o, o,
    y, y, y, y, y, y, y, o,
    y, y, y, y, y, y, o, o,
    y, y, y, y, y, b, o, o,
    y, y, y, y, y, b, o, o,
    y, y, y, y, y, y, o, o,
    y, y, y, y, y, y, y, o,
    o, y, y, y, y, y, o, o
]

pacman4 = [
    o, y, y, y, y, y, o, o,
    y, y, y, y, y, y, y, o,
    y, y, y, y, y, y, y, o,
    y, y, y, y, y, y, o, o,
    y, y, y, y, y, y, o, o,
    y, y, y, y, y, y, y, o,
    y, y, y, y, y, y, y, o,
    o, y, y, y, y, y, o, o
]

pacman5 = [
    o, y, y, y, y, y, o, o,
    y, y, y, y, y, y, y, o,
    y, y, y, y, y, y, y, o,
    y, y, y, y, y, y, y, o,
    y, y, y, y, y, y, y, o,
    y, y, y, y, y, y, y, o,
    y, y, y, y, y, y, y, o,
    o, y, y, y, y, y, o, o
]

pacman6 = [
    o, y, y, y, y, y, o, o,
    y, y, y, y, y, y, y, o,
    y, y, y, y, y, y, y, o,
    y, y, y, y, y, y, o, o,
    y, y, y, y, y, y, o, o,
    y, y, y, y, y, y, y, o,
    y, y, y, y, y, y, y, o,
    o, y, y, y, y, y, o, o
]

pacman7 = [
    o, y, y, y, y, y, o, o,
    y, y, y, y, y, y, y, o,
    y, y, y, y, y, y, o, o,
    y, y, y, y, y, o, o, o,
    y, y, y, y, y, o, o, o,
    y, y, y, y, y, y, o, o,
    y, y, y, y, y, y, y, o,
    o, y, y, y, y, y, o, o
]

pacman8 = [
    o, y, y, y, y, y, o, o,
    y, y, y, y, y, y, o, o,
    y, y, y, y, y, o, o, o,
    y, y, y, y, o, o, o, b,
    y, y, y, y, o, o, o, b,
    y, y, y, y, y, o, o, o,
    y, y, y, y, y, y, o, o,
    o, y, y, y, y, y, o, o
]


def main():
    sense = SenseHat()
    
    while True:
        sense.set_pixels(pacman1)
        sleep(0.125)
        sense.set_pixels(pacman2)
        sleep(0.125)
        sense.set_pixels(pacman3)
        sleep(0.125)
        sense.set_pixels(pacman4)
        sleep(0.125)
        sense.set_pixels(pacman5)
        sleep(0.125)
        sense.set_pixels(pacman6)
        sleep(0.125)
        sense.set_pixels(pacman7)
        sleep(0.125)
        sense.set_pixels(pacman8)
        sleep(0.125)


if __name__ == "__main__":
    main()