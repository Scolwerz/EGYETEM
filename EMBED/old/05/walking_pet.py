from sense_hat import SenseHat
import time
import math

sense = SenseHat()

c_w = (255, 255, 255)     # white
c_y = (255, 255, 0)       # yellow
c_p = (255, 0, 255)       # purple
c_b = (0, 0, 255)         # blue

pet_1 = [
    c_w,c_w,c_w,c_w,c_w,c_w,c_w,c_w,
    c_p,c_w,c_w,c_w,c_w,c_w,c_w,c_w,
    c_w,c_p,c_w,c_w,c_p,c_w,c_p,c_w,
    c_w,c_p,c_b,c_b,c_p,c_y,c_y,c_w,
    c_w,c_b,c_b,c_b,c_y,c_w,c_y,c_b,
    c_w,c_b,c_b,c_b,c_b,c_y,c_y,c_w,
    c_w,c_b,c_w,c_b,c_w,c_b,c_w,c_w,
    c_w,c_w,c_w,c_w,c_w,c_w,c_w,c_w ]

pet_2 = [
    c_w,c_w,c_w,c_w,c_w,c_w,c_w,c_w,
    c_p,c_w,c_w,c_w,c_w,c_w,c_w,c_w,
    c_w,c_p,c_w,c_w,c_p,c_w,c_p,c_w,
    c_w,c_p,c_b,c_b,c_p,c_y,c_y,c_w,
    c_w,c_b,c_b,c_b,c_y,c_w,c_y,c_b,
    c_w,c_b,c_b,c_b,c_b,c_y,c_y,c_w,
    c_w,c_w,c_b,c_w,c_b,c_w,c_w,c_w,
    c_w,c_w,c_w,c_w,c_w,c_w,c_w,c_w ]


def animate_pet():
    for _ in range(3):
        sense.set_pixels(pet_1)
        time.sleep(0.5)
        sense.set_pixels(pet_2)
        time.sleep(0.5)

def get_force():
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    F = math.sqrt(x**2 + y**2 + z**2)
    return F

def main():
    threshold = 1.5
    while True:
        force = get_force()
        if force > threshold:
            animate_pet()
        time.sleep(0.1)


if __name__ == "__main__":
    main()
