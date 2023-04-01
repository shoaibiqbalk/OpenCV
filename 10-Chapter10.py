# Mirroring Video Multiple time

import cv2 as cv
import numpy as np
from cv2 import cvtColor


cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    width = int(cap.get(3))
    height = int(cap.get(4))


    cv.imshow('Frame', frame)

    if cv.waitKey(2) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()