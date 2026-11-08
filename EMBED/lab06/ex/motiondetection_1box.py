
from imutils.video import VideoStream
import datetime
import imutils
import time
import cv2

# T is the threshold of image binarization while min_area defines
# the minimum contour area to insignificant contour suppression
T = 30
min_area = 1000
background = None
video_path = None

# You can use pre-recorded video or the camera as data source
if video_path is None:
    vs = VideoStream().start()
    # warm up the camera
    time.sleep(2)
else:
    vs = cv2.VideoCapture(video_path)

# Read images one by one from the video source:
while True:
    frame = vs.read()
    frame = frame if video_path is None else frame[1]
    # this variable keeps track the state of motion detection
    state = "No change"
    
    # if there is no more frame in the video break the loop
    if frame is None:
        break

    # Resize the frame, convert it to gray scale, and blur (or filter)
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #smooting image in 21x21 pixels regions
    gray = cv2.GaussianBlur(gray, (21,21), 0)
    
    ######################################################################
    # Now we also use the first frame of the video stream as the initial
    # background but now the background is stored as a float array
    if background is None:
        background = gray.copy().astype("float")
        continue
    ######################################################################
    
    ######################################################################
    # Convert back the float background array into byte array (grayscale image)
    delta_frame = cv2.absdiff(gray, cv2.convertScaleAbs(background))
    ######################################################################
    threshold = cv2.threshold(delta_frame, T, 255, cv2.THRESH_BINARY)[1]
    threshold = cv2.dilate(threshold, None, iterations=2)
    
    # On the thresholded image, we can apply contour detection to find outlines of white region(s) (moving objec
    cnts = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    # Only those contours will be taken consider which have greater area than a predefined minimum value. If thi
    valid_cnts = []
    for c in cnts:
        if not cv2.contourArea(c) < min_area:
            valid_cnts.append(c)
    
    if valid_cnts:
        (x, y, w, h) = cv2.boundingRect(cv2.convexHull(cv2.vconcat(valid_cnts)))
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        state = "New object"
    
    ######################################################################
    # Accumulate the weighted average between the current frame
    # and earlier frames. Here the weight value is 0.1.
    cv2.accumulateWeighted(gray, background, 0.1)
    ######################################################################
    
    # The output image is extended with the status of the motion detection and a timestamp
    cv2.putText(frame, "Room Status: {}".format(state), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    cv2.imshow("Camera image", frame)
    cv2.imshow("Threshold", threshold)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("q"):
        break
    
# shut down the camera and close all open windows
vs.stop() if video_path is None else vs.release()
cv2.destroyAllWindows()
