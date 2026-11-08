import cv2
import time
import numpy as np
import imutils
from imutils.video import VideoStream

# Define some necessary variables and constants. The buffsize constant
# defines how many earlier center points will be stored to draw the motion
# track while the indx variable keeps tracks the index of the last stored point
video_path = None
buffsize = 64
indx = 0

# The key of this colored object tracking is a "color filter" where the
# filter will keep only those pixels of the image which fall into a predefined color range.
# The color range can be defined by its lower and upper boundaries. The adjustment in this
# sample code assumes green object(s). In addition, here we initialize a numpy array which
# will store previous (x, y) coordinates of the object center to visualize the object's movement.
green_range = [(25, 55, 5), (65, 255, 255)]
#initialize the list of tracked points
path = np.zeros((buffsize, 2), dtype='int')

video_path = None
if video_path is None:
    vs = VideoStream().start()
    time.sleep(2)
else:
    vs = cv2.VideoCapture(video_path)


while True:
    frame = vs.read()
    frame = frame if video_path is None else frame[1]

    # Resize the frame, blur (or filter) it, and convert it into the HSV (Hue, Saturation, Value)
    # color space (more information about the HSV space: https://en.wikipedia.org/wiki/HSL_and_HSV)
    frame = imutils.resize(frame, width=500)
    blur = cv2.GaussianBlur(frame, (9,9), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    # In this step we create a binary image (mask) using the above defined range.
    # In the mask all pixels that are out of the range will be 0. Moreover, a
    # morphological opening (erosion before dilation) operation will be performed on
    # the mask to remove all small noises that may remained in the mask
    mask = cv2.inRange(hsv, green_range[0], green_range[1])
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Apply contour detection on the mask
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    if len(cnts) > 0:
        # find the largest contour in the mask
        cnt = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(cnt)

        # To determine the centroid of an object, we use its moments
        # (more info: https://www.learnopencv.com/shape-matching-using-hu-moments-c-python/)
        M = cv2.moments(cnt)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # Draw a cycle around the circular object if its radius is higher than the predefined
        # threshold value. In addition, draw another filled cycle around the center of the object
        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

            # If the earlier defined numpy array (our point buffer) is full, shift it one element
            # to the left and past the new center point at the end of the array
            if indx < buffsize:
                path[indx] = (center[0], center[1])
                indx += 1
            else:
                path[0:indx-1] = path[1:indx]
                path[indx-1] = (center[0], center[1])

    # Draw the movement track of the object onto the image. The movement track is visualized as a sequence
    # of connected lines where the thickness of lines depends on its endpoint indexes in the array
    for i in range(1, len(path)):
        # if either of the tracked points are None, ignore them
        if path[i - 1] is None or path[i] is None:
            continue
        # otherwise, compute thickness and draw lines
        thickness = int(np.sqrt(len(path) / float(i + 1)) * 2.5)
        cv2.line(frame, (path[i-1][0], path[i-1][1]), (path[i][0], path[i][1]), (0, 0, 255), thickness)

    cv2.imshow("Image", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break


vs.stop() if video_path is None else vs.release()
cv2.destroyAllWindows()
