from sense_hat import SenseHat

def main():
    sense = SenseHat()
    sense.show_message("Hello world", scroll_speed=0.05, text_colour = (255,0,0), back_colour=(0,0,255))


if __name__ == "__main__":
    main()
