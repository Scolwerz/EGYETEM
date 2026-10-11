from imutils.video import VideoStream
import datetime
import imutils
import time
import cv2
import numpy as np


video_path = None
buffsize = 64
indx = 0

# lower and upper boundaries of a "red" object in HSV color space
red_range = [(0, 120, 70), (10, 255, 255), (170, 120, 70), (180, 255, 255)]
#initialize the list of tracked points
path = np.zeros((buffsize, 2), dtype='int')

video_path = None
if video_path is None:
    vs = VideoStream().start()
    # warm up the camera
    time.sleep(2)
else:
    vs = cv2.VideoCapture(video_path)

while True:
    frame = vs.read()
    frame = frame if video_path is None else frame[1]
    # if there is no more frame in the video break the loop
    if frame is None:
        break

    frame = imutils.resize(frame, width=500)
    blur = cv2.GaussianBlur(frame, (9,9), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    mask1 = cv2.inRange(hsv, red_range[0], red_range[1])
    mask2 = cv2.inRange(hsv, red_range[2], red_range[3])
    mask = cv2.bitwise_or(mask1, mask2)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    if len(cnts) > 0:
        # find the largest contour in the mask
        cnt = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(cnt)

        M = cv2.moments(cnt)
        #center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if M["m00"] > 0:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        else:
            center = None

        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
            # update the path list
            if indx < buffsize:
                path[indx] = (center[0], center[1])
                indx += 1
            else:
                path[0:indx-1] = path[1:indx]
                path[indx-1] = (center[0], center[1])
    #####
    else:
        # clearif no object is detected
        path = np.zeros((buffsize, 2), dtype='int')
        indx = 0


    for i in range(1, len(path)):
        # if either of the tracked points are None, ignore them
        if path[i - 1] is None or path[i] is None:
            continue
        ### if path[i - 1][0] == 0 or path[i][0] == 0:  # skip uninitialized points

        # otherwise, compute thickness and draw lines
        thickness = int(np.sqrt(len(path) / float(i + 1)) * 2.5)
        cv2.line(frame, (path[i-1][0], path[i-1][1]), (path[i][0], path[i][1]), (0, 0, 255), thickness)

        #####
        thickness = int((len(path) - i) / len(path) * 10) + 1
        cv2.line(frame, (path[i-1][0], path[i-1][1]), (path[i][0], path[i][1]), (0, 0, 255), thickness)


    cv2.imshow("Delta frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

# shut down the camera and close all open windows
vs.stop() if video_path is None else vs.release()
cv2.destroyAllWindows()
