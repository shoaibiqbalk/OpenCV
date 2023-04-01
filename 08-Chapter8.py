# Cam Image

import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv.imshow('Frame', frame)

    if cv.waitKey(2) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()