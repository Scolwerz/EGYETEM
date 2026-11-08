"""
sudo rapsi-config

/boot/firmware/config.txt 
    [all] dtoverlay=w1-gpio -> [all] dtoverlay=w1-gpio, gpiopin=18

sudo reboot

sensor address: 
ls /sys/bus/w1/devices/
---> 28-xxx
"""

import RPi.GPIO as io
import time

io.setmode(io.BCM)

def temperature_measurement():
    # Open and read the content of the file
    tempfile = open("/sys/bus/w1/devices/28-00000b74781b/w1_slave")
    thetext = tempfile.read()
    tempfile.close()

    # Temperature information can be found at the end of the 2. row
    tempdata = thetext.split("\n")[1].split(" ")[-1]
    temperature = round(float(tempdata[2:]) / 1000.0, 1)
    return temperature



# Read temperature values continuously
while True:
    t = temperature_measurement()
    print("Temperature: {} C".format(t))
    time.sleep(1)
