from sense_hat import SenseHat

w = (255, 255, 255)     # white
b = (0, 0, 255)         # blue

smiley_pixels = [
    w, w, w, w, w, w, w, w,
    w, b, b, w, w, b, b, w,
    w, b, b, w, w, b, b, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, b, w, w, w, w, b, w,
    w, w, b, b, b, b, w, w,
    w, w, w, w, w, w, w, w]

def main():
    sense = SenseHat()
    sense.set_pixels(smiley_pixels)


if __name__ == "__main__":
    main()
