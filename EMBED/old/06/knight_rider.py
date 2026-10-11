from sense_hat import SenseHat
import time

sense = SenseHat()

p = [2,3]
light_len = 3
space_size = 8
speed = 1/7

r = (255,0,0)
n = (0,0,0)

space = [
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    r, r, r, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n ]

direction =  1


def shift_right():
    global p
    sense.clear()

    p[0] += 1
    for i in range(p[0]-light_len+1, p[0]+1):
        sense.set_pixel(i, p[1], r)
    #for i in range(light_len):
    #    if p[0] - light_len + 1 + i < space_size:
    #        sense.set_pixel(p[0] - light_len + 1 + i, p[1], r)


def shift_left():
    global p
    sense.clear()

    p[0] -= 1
    for i in range(p[0]-light_len+1, p[0]+1):
        sense.set_pixel(i, p[1], r)
    #for i in range(light_len):
    #    if p[0] + i >= 0:
    #        sense.set_pixel(p[0] + i - 1, p[1], r)


def main():
    global p
    while True:
        while True: #2-7
            shift_right()
            time.sleep(speed)
            if p[0] == space_size-1: break

        while True: #7-2
            shift_left()
            time.sleep(speed)
            if p[0] == light_len-1: break



if __name__ == "__main__":
    main()
