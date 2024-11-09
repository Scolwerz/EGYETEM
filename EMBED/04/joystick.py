from sense_hat import SenseHat
import time

w = (255, 255, 255)     # white
r = (255, 0, 0)         # red

arrow = [
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, r, w, w, w, w,
    w, w, w, w, r, w, w, w,
    w, r, r, r, r, r, w, w,
    w, w, w, w, r, w, w, w,
    w, w, w, r, w, w, w, w,
    w, w, w, w, w, w, w, w,]


def main():
    sense = SenseHat()

    while True:
        for event in sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "up":
                    sense.set_rotation(270)
                    sense.set_pixels(arrow)
                elif event.direction == "down":
                    sense.set_rotation(90)
                    sense.set_pixels(arrow)
                elif event.direction == "left":
                    sense.set_rotation(180)
                    sense.set_pixels(arrow)
                elif event.direction == "right":
                    sense.set_rotation(0)
                    sense.set_pixels(arrow)
                elif event.direction == "middle":
                    sense.set_rotation(0)
                    sense.show_letter("M")
                time.sleep(0.5)
                sense.clear()


if __name__ == "__main__":
    main()
