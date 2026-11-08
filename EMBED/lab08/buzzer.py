import RPi.GPIO as io
import time

buzzer_pin = 24

# Use the Broadcom (BCM) GPIO numbering scheme.
io.setmode(io.BCM)

# Configure the GPIO pin connected to the buzzer as an output pin.
io.setup(buzzer_pin, io.OUT)

def play(pitches, durations):
    for pitch, duration in zip(pitches, durations):
        # convert duration from ms to s
        duration *= 0.001

        if (pitch == 0):
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


# Notes: E5, E5, pause, E5, pause, C5, E5, pause, G5, pause, G4, ...
pitches = [659, 659, 0, 659, 0, 523, 659, 0, 784, 0, 392,
523, 0, 392, 0, 330, 0, 440, 0, 494, 0, 466, 440]

durations = [150, 150, 150, 150, 150, 150, 150, 150, 300, 300, 300,
300, 150, 300, 150, 300, 150, 150, 150, 150, 150, 150, 300]

play(pitches, durations)
