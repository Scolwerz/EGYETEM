import RPi.GPIO as io
import time

TRIG = 17
ECHO = 27
MAX_DURATION = 38000

io.setmode(io.BCM)
io.setup(TRIG,io.OUT) # trig
io.setup(ECHO,io.IN) # echo

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



# Measure distance continuously
while True:
    d = ultrasonic_measurement()
    print("Distance: {} cm".format(d if d > 0 else '-'))
    time.sleep(1)
