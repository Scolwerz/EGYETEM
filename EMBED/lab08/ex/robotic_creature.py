
import RPi.GPIO as io
import time
import math

# GPIO pins
led_b = 16
led_r = 20
led_g = 21
buzzer_pin = 24
photo_pin = 23

TRIG = 17
ECHO = 27
MAX_DURATION = 38000

# Photoresistor settings
C = 0.00001
Rmax = 10000
Tmax = Rmax * C
Vs = 1.95

# Adjust this value according to measurements
DARK_THRESHOLD = 10000


io.setmode(io.BCM)

# RGB LED setup
io.setup(led_r, io.OUT)
io.setup(led_g, io.OUT)
io.setup(led_b, io.OUT)

# Buzzer setup
io.setup(buzzer_pin, io.OUT)

# Ultrasonic sensor setup
io.setup(TRIG, io.OUT)
io.setup(ECHO, io.IN)

# Set RGB LED color
def set_color(red, green, blue):
    io.output(led_r, red)
    io.output(led_g, green)
    io.output(led_b, blue)


pitches = [659, 784, 880, 784, 659]
durations = [150, 150, 200, 150, 300]
def play_melody(pitches, durations):
    for pitch, duration in zip(pitches, durations):
        # convert duration from ms to s
        duration *= 0.001

        if (pitch == 0):
            io.output(buzzer_pin, io.LOW)
            time.sleep(duration)
        else:
            period = 1.0 / pitch
            delay = period / 2

        # the buzzer should sound for ~90% of the duration
        cycles = int(0.9 * duration * pitch)

        # Generate PWM signal "manually"
        for i in range(cycles):
            io.output(buzzer_pin, True)
            time.sleep(delay)
            io.output(buzzer_pin, False)
            time.sleep(delay)

        # no sound in 10% of duration
        time.sleep(0.1 * duration)

def play_tone(pitch, duration):
    play_melody([pitch], [duration])


# Measure distance using the ultrasonic sensor
def ultrasonic_measurement():
    # Take the trigger line into idle state
    # and keep distance (in time) between measurements
    io.output(TRIG, io.LOW)
    time.sleep(0.05)

    # Generate a trigger event
    io.output(TRIG, io.HIGH)
    time.sleep(0.00001)
    io.output(TRIG, io.LOW)

    # Waiting for echo signal
    while io.input(ECHO) == 0:
        pass

    # Measuring the time while the echo signal is in hight state
    pulse_start = time.perf_counter_ns()
    while io.input(ECHO) == 1:
        pass

    duration_us = (time.perf_counter_ns() - pulse_start) / 1000.0
    distance = round(duration_us / 58.0, 2) if MAX_DURATION > duration_us else 0.0
    return distance


# Measure photoresistor resistance
def photoresistor_measurement():
    io.setup(photo_pin, io.OUT)
    io.output(photo_pin, io.HIGH)
    time.sleep(5 * Tmax)

    io.setup(photo_pin, io.IN)
    start_time = time.time()

    while io.input(photo_pin) == io.HIGH:
        pass

    dt = time.time() - start_time
    resistance = - (0.85 * dt / (C * math.log(1.0 - (Vs / 3.3))))
    return resistance





greeted = False

while True:
    light = photoresistor_measurement()
    distance = ultrasonic_measurement()
    print("Light resistance: {:.1f} Ohm".format(light))
    print("Distance: {} cm".format(distance if distance > 0 else '-'))


    # Sleep in darkness
    if light > DARK_THRESHOLD:
        set_color(0, 0, 0)
        io.output(buzzer_pin, io.LOW)
        greeted = False

    # Frightened when an object gets too close
    elif 0 < distance <= 20:
        greeted = False
        for i in range(5):
            set_color(1, 0, 0)
            # Rapid beep
            play_tone(1200, 100)
            set_color(0, 0, 0)
            time.sleep(0.1)

    # Wake up when an object approaches
    elif 20 < distance <= 50:
        set_color(0, 0, 1)
        if not greeted:
            play_melody(pitches, durations)
            greeted = True
        io.output(buzzer_pin, io.LOW)

    # Waiting for an approaching object
    else:
        # Waiting for an approaching object
        set_color(0, 1, 0)
        io.output(buzzer_pin, io.LOW)
        greeted = False

    time.sleep(0.2)
