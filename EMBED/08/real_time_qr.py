from imutils.video import VideoStream
import imutils
import time
import cv2
from pyzbar import pyzbar
import argparse


# Set up argument parser for Pi camera selection
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--picamera", type=int, default=-1, help="Pi camera or USB camera will be used")
args = vars(ap.parse_args())

# Start video stream (using Pi camera if specified)
vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)

# Process video stream frame-by-frame
while True:
    # Acquire frame from video stream
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    # Detect barcodes and QR codes
    barcodes = pyzbar.decode(frame)

    # Loop over detected barcodes/QRs
    for barcode in barcodes:
        # Draw bounding box around detected code
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Convert barcode data to string and get its type
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        # Draw barcode data and type on the frame
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 0, 255), 2)


    # Display the frame with detected codes
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # If the `q` key is pressed, exit the loop
    if key == ord("q"):
        break

# Clean up: close window and stop video stream
cv2.destroyAllWindows()
vs.stop()
