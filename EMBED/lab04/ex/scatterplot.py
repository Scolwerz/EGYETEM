from sense_hat import SenseHat
import matplotlib.pyplot as plt
import math
from time import sleep

data_acquisition = True

def stop():
    global data_acquisition
    data_acquisition = False


def main():
    sense = SenseHat()

    sense.stick.direction_middle = stop
    
    print("Start data acquisition...")
    print("Rotate around the z-axis.")
    print("Press joy when finished.")

    x_values = []
    y_values = []
    while data_acquisition:
            magnet = sense.get_compass_raw()

            x = magnet["x"]
            y = magnet["y"]
            x_values.append(x)
            y_values.append(y)

            print("x: {:.2f}, y: {:.2f}".format(x, y))
            sleep(0.1)

    print("\nData acquisition stopped.")
    
    plt.scatter(x_values, y_values, color="red", s=8)
    plt.title("Magnetic Sensor X-Y Scatter Plot")
    plt.xlabel("Magnet X")
    plt.ylabel("Magnet Y")
    plt.grid(True)
    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    main()
