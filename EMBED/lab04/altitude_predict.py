from sense_hat import SenseHat
import math

P0 = 1022

def main():
    sense = SenseHat()

    p = round(sense.get_pressure(), 1)

    h = 44330 * (1.0 - (p / P0) ** (0.1903))
    print(f"Atmospheric Pressure: {p:.2f} hPa")
    print(f"Altitude: {h:.2f} meters")


if __name__ == "__main__":
    main()
