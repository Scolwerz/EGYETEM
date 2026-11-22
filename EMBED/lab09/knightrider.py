import numpy as np
import time
import smbus

# Initialize the I2C bus
bus = smbus.SMBus(1) # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

# MCP23017 IC address
DEVICE = 0x20

# The I/O Direction Registers (IODIRx) are used to configure the data direction of the GPIO pins.
# To configure the pins of a bank as either inputs or outputs, a hexadecimal value must be written
# to the corresponding I/O direction register. The IODIRA register (address 0x00) controls the pins of Bank A.
# The direction of each pin is determined by the value of its corresponding bit in the register:
# a value of 1 configures the pin as an input, whereas a value of 0 configures it as an output.
IODIRA = 0x00

# The OLAT (Output Latch Register) provides access to the output latches. Writing data to this register
# updates the state of the output pins, allowing the LEDs connected to the port to be controlled.
OLATA = 0x14

# Port A be output
bus.write_byte_data(DEVICE, IODIRA, 0)


def knight_rider():
    # Statically defined running light in matrix form where there are as many columns as LEDs
    # and consists of as many rows as the number of defined illumination states. Since the light sequence
    # moves back and forth, the matrix is composed of 2x12 rows (12 forward and 12 backward states).
    m = np.array([[9, 0, 0, 0, 0, 0, 0, 0],
        [9, 9, 0, 0, 0, 0, 0, 0],
        [5, 9, 9, 0, 0, 0, 0, 0],
        [2, 5, 9, 9, 0, 0, 0, 0],
        [1, 2, 5, 9, 9, 0, 0, 0],
        [0, 1, 2, 5, 9, 9, 0, 0],
        [0, 0, 1, 2, 5, 9, 9, 0],
        [0, 0, 0, 1, 2, 5, 9, 9],
        [0, 0, 0, 0, 1, 2, 5, 9],
        [0, 0, 0, 0, 0, 1, 2, 5],
        [0, 0, 0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 0, 0, 0, 1],
        
        [0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 9, 9],
        [0, 0, 0, 0, 0, 9, 9, 5],
        [0, 0, 0, 0, 9, 9, 5, 2],
        [0, 0, 0, 9, 9, 5, 2, 1],
        [0, 0, 9, 9, 5, 2, 1, 0],
        [0, 9, 9, 5, 2, 1, 0, 0],
        [9, 9, 5, 2, 1, 0, 0, 0],
        [9, 5, 2, 1, 0, 0, 0, 0],
        [5, 2, 1, 0, 0, 0, 0, 0],
        [2, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0]])
    
    bus.write_byte_data(DEVICE,OLATA,0)

    try:
        while(True):
            for i in range(len(m)):
                for j in range(9):
                    leds = 0
                    for l in range(8):
                        if j < m[i][l]:
                            leds += 2**l
                    
                    bus.write_byte_data(DEVICE, OLATA, leds)
                    time.sleep(0.006)
    except KeyboardInterrupt:
        # Reset LED states
        bus.write_byte_data(DEVICE, OLATA, 0)
    
knight_rider()
