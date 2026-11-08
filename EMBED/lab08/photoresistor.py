import RPi.GPIO as io
import time
import math

pin = 23
C = 0.00001
Rmax = 10000
Tmax = Rmax*C
Vs = 1.95

io.setmode(io.BCM)

def rc_timing(pin):
    # Charging --> time >= 5T
    io.setup(pin, io.OUT)
    io.output(pin, io.HIGH)
    time.sleep(5*Tmax)
    
    # Discharging
    io.setup(pin, io.IN)
    start_time = time.time()

    # Waiting for incomming 0 --> Vin <= Vs
    while (io.input(pin) == io.HIGH):
        pass
    dt = time.time() - start_time
    return - (0.85*dt / (C * math.log(1.0 - (Vs / 3.3))))


# Take 5 delayed measurements
for i in range(5):
    R = rc_timing(pin)
    print("Resistance: {:.1f} kOhm".format(R / 1000))
    time.sleep(1)
