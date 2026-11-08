import RPi.GPIO as io
import time

led_b = 16
led_r = 20
led_g = 21

io.setmode(io.BCM)
io.setup(led_r, io.OUT) # red
io.setup(led_g, io.OUT) # green
io.setup(led_b, io.OUT) # blue

def pulsation(up = True):
    f = 50
    period = 1.0 / f

    if up:
        i1 = 0
        i2 = f
        step = 1
    else:
        i1 = f
        i2 = 0
        step = -1

    # Generate PWM signal "manually"
    for i in range(i1, i2, step):
        p = i / f
        io.output(led_r, io.HIGH)
        io.output(led_g, io.HIGH)
        io.output(led_b, io.HIGH)
        time.sleep(p * period)

        io.output(led_r, io.LOW)
        io.output(led_g, io.LOW)
        io.output(led_b, io.LOW)
        time.sleep((1-p) * period)



while True:
    pulsation(True)
    pulsation(False)
