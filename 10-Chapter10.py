# Drawing Shapes and Text

import cv2 as cv
import numpy as np
from cv2 import cvtColor


cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv.line(frame, (0, 0), (width, height), (255, 0, 0), 10) # Drawing line
    img = cv.rectangle(img, (100, 100), (200, 200), (200, 0, 0), 5) # Drawing Rectangle
    img = cv.circle(img, (300, 300), 60, (0, 0, 255), 5) # Drawing Circle
    font = cv.FONT_HERSHEY_COMPLEX
    img = cv.putText(img, 'This is Text', (10, height-10), font, 2, (0, 0, 0), 4, cv.LINE_AA) # Text

    cv.imshow('Frame', img)

    if cv.waitKey(2) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()