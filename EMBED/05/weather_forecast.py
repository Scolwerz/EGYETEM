from sense_hat import SenseHat
import time

sense = SenseHat()

h = 125
p_threshold = 1.6
time_interval = 15

forecast_falling = [
    "Settled Fine", "Fine Weather", "Fine, Becoming Less Settled",
    "Fairly Fine, Showery Later", "Showery, Becoming More Unsettled",
    "Unsettled, Rain Later", "Rain at Times, Worse Later",
    "Rain at Times, Becoming Very Unsettled", "Very Unsettled, Rain" ]

forecast_steady = [
    "Settled Fine", "Fine Weather", "Fine, Possibly Showers",
    "Fairly Fine, Showers Likely", "Showery, Bright Intervals",
    "Changeable, Some Rain", "Unsettled, Rain at Times",
    "Rain at Frequent Intervals", "Very Unsettled, Rain" ]

forecast_rising = [
    "Settled Fine", "Fine Weather", "Becoming Fine" ]


def sea_level_pressure(P, T, h=h):
    P0 = P * (1 - (0.0065 * h) / (T + 0.0065 * h + 273.15)) ** (-5.257)
    return P0

def get_forecast_number(P0, tendency):
    if tendency == "falling" and 985 <= P0 <= 1050:
        Z = 127 - 0.12 * P0
        forecast = forecast_falling[int(Z) - 1]
    elif tendency == "steady" and 960 <= P0 <= 1033:
        Z = 144 - 0.13 * P0
        forecast = forecast_steady[int(Z) - 10]
    elif tendency == "rising" and 947 <= P0 <= 1030:
        Z = 185 - 0.16 * P0
        forecast = forecast_rising[int(Z) - 20]
    else:
        forecast = "Unable to predict the weather"
    return forecast


def main():

    p = sense.get_pressure()
    t = sense.get_temperature()
    p0 = sea_level_pressure(p, t, h)

    time.sleep(time_interval)

    p_new = sense.get_pressure()
    t_new = sense.get_temperature()
    p0_new = sea_level_pressure(p_new, t_new, h)

    p_diff = p0_new - p0
    if p_diff < -p_threshold:   tendency = "falling"
    elif p_diff > p_threshold:  tendency = "rising"
    else:                       tendency = "steady"
    print(f"Pressure tendency: {tendency}")

    forecast = get_forecast_number(p0_new, tendency)
    print(f"Weather forecast: {forecast}")

    sense.show_message(forecast, scroll_speed=0.05)



if __name__ == "__main__":
    main()
