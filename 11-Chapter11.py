# Capturing specific color in frame

import cv2 as cv
import numpy as np
from cv2 import cvtColor


cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask = cv.inRange(hsv, lower_blue, upper_blue)
    result = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('Frame', result)

    if cv.waitKey(2) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()