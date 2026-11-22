
import time
import smbus
import spidev
import random


# Initialize the I2C bus
bus = smbus.SMBus(1) # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

DEVICE = 0x20

IODIRA = 0x00
IODIRB = 0x01
GPIOB = 0x13
OLATA = 0x14

bus.write_byte_data(DEVICE, IODIRA, 0x00)
bus.write_byte_data(DEVICE, IODIRB, 0xFF)


spi = spidev.SpiDev() # create spi object
spi.open(0, 0) # open spi port 1, device (CS) 0
spi.max_speed_hz = 1000000

MAX7219_REG_NOOP = 0x0
MAX7219_REG_DIGIT0 = 0x1
MAX7219_REG_DIGIT1 = 0x2
MAX7219_REG_DIGIT2 = 0x3
MAX7219_REG_DIGIT3 = 0x4
MAX7219_REG_DIGIT4 = 0x5
MAX7219_REG_DIGIT5 = 0x6
MAX7219_REG_DIGIT6 = 0x7
MAX7219_REG_DIGIT7 = 0x8
MAX7219_REG_DECODEMODE = 0x9
MAX7219_REG_INTENSITY = 0xA
MAX7219_REG_SCANLIMIT = 0xB
MAX7219_REG_SHUTDOWN = 0xC
MAX7219_REG_DISPLAYTEST = 0xF

def initialize_seven_segment(intensity=0x8):
    # During initialization, the display brightness (intensity) must be configured.
    # BCD decoding is not used - REG_DECODEMODE
    # Two digits will be used - REG_SCANLIMIT
    # Normal operating mode - REG_SHUTDOWN
    spi.xfer([MAX7219_REG_DECODEMODE, 0x0])
    spi.xfer([MAX7219_REG_INTENSITY, intensity])
    spi.xfer([MAX7219_REG_SCANLIMIT, 0x1])
    spi.xfer([MAX7219_REG_SHUTDOWN, 0x1])


seg = {"a": 64, "b": 32, "c": 16, "d": 8, "e": 4, "f": 2, "g": 1}
digits = [seg["a"]+seg["b"]+seg["c"]+seg["d"]+seg["e"]+seg["f"],
    seg["b"]+seg["c"],
    seg["a"]+seg["b"]+seg["d"]+seg["e"]+seg["g"],
    seg["a"]+seg["b"]+seg["c"]+seg["d"]+seg["g"],
    seg["b"]+seg["c"]+seg["f"]+seg["g"],
    seg["a"]+seg["c"]+seg["d"]+seg["f"]+seg["g"],
    seg["a"]+seg["c"]+seg["d"]+seg["e"]+seg["f"]+seg["g"],
    seg["a"]+seg["b"]+seg["c"],
    seg["a"]+seg["b"]+seg["c"]+seg["d"]+seg["e"]+seg["f"]+seg["g"],
    seg["a"]+seg["b"]+seg["c"]+seg["d"]+seg["f"]+seg["g"]]

def show_segment_number(number):
    number = round(number, 1)
    if number < 10:
        dig0 = int(number)
        spi.xfer([MAX7219_REG_DIGIT0, digits[dig0] | 0x80])

        dig1 = int((number - dig0) * 10)
        spi.xfer([MAX7219_REG_DIGIT1, digits[dig1]])
    else:
        print("[ERROR] The number is greater than 9.9")
        spi.xfer([MAX7219_REG_DIGIT0, seg["g"]])
        spi.xfer([MAX7219_REG_DIGIT1, seg["g"]])



initialize_seven_segment()

bus.write_byte_data(DEVICE, OLATA, 0)
time.sleep(1 + 3*random.random())
bus.write_byte_data(DEVICE, OLATA, 1)

start_time = time.perf_counter()
while True:
    button = bus.read_byte_data(DEVICE, GPIOB)
    if button & 0x01:
        reaction_time = time.perf_counter() - start_time
        bus.write_byte_data(DEVICE, OLATA, 0)
        show_segment_number(reaction_time)
        print("Reaction time: {:.1f} sec".format(reaction_time))
        break

time.sleep(3)

bus.write_byte_data(DEVICE, OLATA, 0)
spi.xfer([MAX7219_REG_DIGIT0, 0])
spi.xfer([MAX7219_REG_DIGIT1, 0])
