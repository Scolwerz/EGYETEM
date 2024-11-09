from sense_hat import SenseHat
import time

sense = SenseHat()

def main():
    while True:
        # Get the current orientation (pitch, roll, yaw)
        o = sense.get_orientation()
        pitch = o["pitch"]
        roll = o["roll"]
        yaw = o["yaw"]

        # Get the raw accelerometer data
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        # Round the accelerometer values
        x = round(x, 0)
        y = round(y, 0)
        z = round(z, 0)

        # Print the orientation and acceleration values
        print("\n\n\nPitch: {}, Roll: {}, Yaw: {}".format(pitch,roll,yaw))
        print("x: {}, y: {}, z: {}".format(x,y,z))

        # Wait for a short time before repeating
        time.sleep(0.5)

if __name__ == "__main__":
    main()
