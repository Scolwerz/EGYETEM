from random import randint
from sense_hat import SenseHat
import time

def random_colour():
    random_red = randint(0, 255)
    random_green = randint(0, 255)
    random_blue = randint(0, 255)
    return (random_red, random_green, random_blue)


def main():
    sense = SenseHat()
    name="DANI"
    for i in range(len(name)):
        sense.show_letter(name[i], random_colour())
        time.sleep(1)
    sense.clear()


if __name__ == "__main__":
    main()
