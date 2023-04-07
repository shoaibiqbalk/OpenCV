## Setting of Camera or Video

import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)

while True:
    ret, frame = cam.read()

    if ret == True:
        cv.imshow("Video", frame)
        # to quite with 'q'
        if cv.waitKey(2) & 0xFF == ord('q'):
            break
    else:
        break

cam.release()
cv.destroyAllWindows()   