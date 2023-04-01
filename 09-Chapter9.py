# Mirroring Video Multiple time

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv.imshow('Frame', frame)

    width = int(cap.get(3))
    height = int(cap.get(4))

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)
    

    if cv.waitKey(2) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()