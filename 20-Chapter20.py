## Resolution of Camera

import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)

# resolution HD (1280 )
def resolution(w, h):
    cam.set(3, w) # 3 is the key to width
    cam.set(4, h) # 4 is the key to height

resolution(1280, 720)

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