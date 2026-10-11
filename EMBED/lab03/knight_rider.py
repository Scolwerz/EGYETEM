from sense_hat import SenseHat
import time

sense = SenseHat()

p = [3,2]
beam_size = 3
row_size = 8
speed = 1/7

r = (255,0,0)
n = (0,0,0)

pixels = [
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
    for i in range(p[0]-beam_size+1, p[0]+1):
        sense.set_pixel(i, p[1], r)
    for i in range(beam_size):
        if p[0] - beam_size + 1 + i < row_size:
            sense.set_pixel(p[0] - beam_size + 1 + i, p[1], r)

def shift_left():
    global p
    sense.clear()

    p[0] -= 1
    for i in range(p[0]-beam_size+1, p[0]+1):
        sense.set_pixel(i, p[1], r)
    #for i in range(light_len):
    #    if p[0] + i >= 0:
    #        sense.set_pixel(p[0] + i - 1, p[1], r)



def shift_right():
    if p[1] < (row_size-1):
        # update p
        p[1] += 1
        #turn on the new pixel
        indx = row_size * p[0] + p[1]
        pixels[indx] = r
        #turn off the tail pixel
        pixels[indx - beam_size] = n
        sense.set_pixels(pixels)
        return True
    else:
        return False

def shift_left():
    if p[1] > (beam_size-1):
        #turn on the new pixel
        indx = row_size * p[0] + p[1]
        pixels[indx - beam_size] = r
        #turn off the tail pixel
        pixels[indx] = n
        # update p
        p[1] -= 1
        sense.set_pixels(pixels)
        return True
    else:
        return False

def light_beam():
    global p
    while True:
        while shift_right():
            time.sleep(speed)
        while shift_left():
            time.sleep(speed)

def main():
    light_beam()
    #global p
    #while True:
    #    while True: #2-7
    #        shift_right()
    #        time.sleep(speed)
    #       if p[0] == row_size-1: break
    #
    #    while True: #7-2
    #        shift_left()
    #        time.sleep(speed)
    #        if p[0] == beam_size-1: break



if __name__ == "__main__":
    main()
