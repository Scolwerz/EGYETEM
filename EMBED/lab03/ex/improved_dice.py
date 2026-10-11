from random import randint
from sense_hat import SenseHat
import time

sense = SenseHat()

o = (0,0,0)
b = (0,0,255)

one_img = [
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,b,b,o,o,o,
    o,o,o,b,b,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o]

two_img = [
    o,o,o,o,o,o,o,o,
    o,b,b,o,o,o,o,o,
    o,b,b,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,b,b,o,
    o,o,o,o,o,b,b,o,
    o,o,o,o,o,o,o,o]

three_img = [
    o,o,o,o,o,o,o,o,
    o,b,b,o,o,o,o,o,
    o,b,b,o,o,o,o,o,
    o,o,o,b,b,o,o,o,
    o,o,o,b,b,o,o,o,
    o,o,o,o,o,b,b,o,
    o,o,o,o,o,b,b,o,
    o,o,o,o,o,o,o,o]

four_img = [
    o,o,o,o,o,o,o,o,
    o,b,b,o,o,b,b,o,
    o,b,b,o,o,b,b,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,b,b,o,o,b,b,o,
    o,b,b,o,o,b,b,o,
    o,o,o,o,o,o,o,o]

five_img = [
    o,o,o,o,o,o,o,o,
    o,b,b,o,o,b,b,o,
    o,b,b,o,o,b,b,o,
    o,o,o,b,b,o,o,o,
    o,o,o,b,b,o,o,o,
    o,b,b,o,o,b,b,o,
    o,b,b,o,o,b,b,o,
    o,o,o,o,o,o,o,o]

six_img = [
    o,b,b,o,o,b,b,o,
    o,b,b,o,o,b,b,o,
    o,o,o,o,o,o,o,o,
    o,b,b,o,o,b,b,o,
    o,b,b,o,o,b,b,o,
    o,o,o,o,o,o,o,o,
    o,b,b,o,o,b,b,o,
    o,b,b,o,o,b,b,o]

dice_images = {
    1: one_img,
    2: two_img,
    3: three_img,
    4: four_img,
    5: five_img,
    6: six_img
}


def number_gen(event):
    if event.action == "pressed":
        for _ in range(30):
            val = randint(1, 6)
            sense.set_pixels(dice_images[val])
            time.sleep(0.1)
        print(val)
        time.sleep(2)
        sense.clear()


def main():
    while True:
        for event in sense.stick.get_events():
            number_gen(event)


if __name__ == "__main__":
    main()
