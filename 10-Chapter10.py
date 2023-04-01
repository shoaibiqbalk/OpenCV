# Drawing Shapes and Text

import cv2 as cv
import numpy as np
from cv2 import cvtColor


cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv.line(frame, (0, 0), (width, height), (255, 0, 0), 10)

    cv.imshow('Frame', img)

    if cv.waitKey(2) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()