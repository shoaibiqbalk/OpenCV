## Setting of Camera or Video

import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)
cam.set(10, 50) # 10 is the key to set brightness
cam.set(3, 640) # 3 is the key to width
cam.set(4, 480) # 4 is the key to height


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