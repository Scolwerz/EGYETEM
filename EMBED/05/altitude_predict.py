from sense_hat import SenseHat
import math

P0 = 1013.25

def calculate_altitude(P, P0=P0):
    altitude = 44331 * (1 - (P / P0) ** (1 / 5.2558))
    return altitude


def main():
    sense = SenseHat()
    p = sense.get_pressure()
    altitude = calculate_altitude(p)
    print(f"Atmospheric Pressure: {p:.2f} hPa")
    print(f"Predicted Altitude: {altitude:.2f} meters")


if __name__ == "__main__":
    main()
