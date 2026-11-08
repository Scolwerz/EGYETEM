
import RPi.GPIO as io
import time

# GPIO pins
led_b = 16
led_r = 20
led_g = 21
buzzer_pin = 24

TRIG = 17
ECHO = 27
MAX_DURATION = 38000

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

def play_buzzer(pitch, duration):
    # convert duration from ms to s
    duration *= 0.001

    if pitch == 0:
        time.sleep(duration)
    else:
        period = 1.0 / pitch
        delay = period / 2

        # The buzzer should sound for ~90% of the duration
        cycles = int(0.9 * duration * pitch)

        # Generate PWM signal manually
        for i in range(cycles):
            io.output(buzzer_pin, True)
            time.sleep(delay)
            io.output(buzzer_pin, False)
            time.sleep(delay)

        # No sound in 10% of duration
        time.sleep(0.1 * duration)



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



while True:
    distance = ultrasonic_measurement()
    print("Distance: {} cm".format(distance if distance > 0 else '-'))

    if distance <= 0:
        set_color(0, 0, 0)

    elif distance > 50:
        # green LED, no sound
        set_color(0, 1, 0)

    elif distance >= 20:
        # yellow LED + buzzer 
        set_color(1, 1, 0)

        # Beeps become more frequent as the object approaches
        delay = 0.1 + (distance - 20) * 0.02
        play_buzzer(1000, 100)
        time.sleep(delay)
        continue

    else:
        # red LED + continuous sound
        set_color(1, 0, 0)
        play_buzzer(1000, 1000)

    time.sleep(0.05)
