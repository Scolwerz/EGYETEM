from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

x = 3
y = 3

o = (0, 0, 0)
r = (255, 0, 0)

thr = 20
sensor_limit = 360


def main():
    while True:
        orientation = sense.get_orientation()
        pitch = orientation["pitch"]

        sense.clear()

        if pitch >= thr and pitch <= sensor_limit/2 - thr:  # jobb [20-160]
            x += 1
        elif pitch >= sensor_limit/2 + thr and pitch <= sensor_limit - thr: # bal [200-340]
            x -= 1

        if x < 0:
            x = 0
        if x > 7:
            x = 7

        sense.set_pixel(x, y, r)

        print("Pitch: {:.2f}, X position: {}".format(pitch, x))
        sleep(0.33)


if __name__ == "__main__":
    main()