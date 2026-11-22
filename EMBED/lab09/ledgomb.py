import RPi.GPIO as io
import smbus
import time

bus = smbus.SMBus(1) # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

# MCP23017 IC address.
DEVICE = 0x20

# Adjust direction of port A
IODIRA = 0x00

# Adjust direction of port B
IODIRB = 0x01

# State of input pins
GPIOB = 0x13

# Write data to port A
OLATA = 0x14

# Port A be output
bus.write_byte_data(DEVICE, IODIRA, 0)


def check_buttons():
    try:
        while True:
            output = 0x00
            sw = bus.read_byte_data(DEVICE, GPIOB)
            for i in range(8):
                mask = 2**i
                output += (sw & mask)
                
            # Show button states on the LEDs
            bus.write_byte_data(DEVICE, OLATA, output)
            time.sleep(0.2)
    except KeyboardInterrupt:
        # Reset LED states
        bus.write_byte_data(DEVICE, OLATA, 0)
        
        
check_buttons()
