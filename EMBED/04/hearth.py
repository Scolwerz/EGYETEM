from sense_hat import SenseHat

w = (255, 255, 255)     # white
r = (255, 0, 0)         # red

heart_pixels = [
    w, w, w, w, w, w, w, w,
    w, r, r, w, w, r, r, w,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    w, r, r, r, r, r, r, w,
    w, w, r, r, r, r, w, w,
    w, w, w, r, r, w, w, w,
    w, w, w, w, w, w, w, w]

def main():
    sense = SenseHat()
    sense.set_pixels(heart_pixels)


if __name__ == "__main__":
    main()
