import numpy as np
import cv2 as cv

# Hardcoded video file path
video_path = "slow_traffic_small.mp4"
cap = cv.VideoCapture(video_path)

# Take first frame of the video
ret, frame = cap.read()

# Setup initial location of window
x, y, w, h = 300, 200, 100, 50  # Hardcoded tracking window
track_window = (x, y, w, h)

# Set up the ROI for tracking
roi = frame[y:y+h, x:x+w]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)

# Setup the termination criteria: either 10 iterations or move by at least 1 pt
term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)

while True:
    ret, frame = cap.read()
    if ret:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        # Apply meanshift to get the new location
        ret, track_window = cv.meanShift(dst, track_window, term_crit)

        # Draw the tracking rectangle
        x, y, w, h = track_window
        img2 = cv.rectangle(frame, (x, y), (x + w, y + h), 255, 2)
        cv.imshow('img2', img2)

        k = cv.waitKey(30) & 0xff
        if k == 27:  # ESC key to exit
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
