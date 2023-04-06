# Face & Eye Detection + Tracking

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

# pre-trained classifier models 
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_eye.xml")


while True:
    ret, frame = cap.read()
    cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('Frame', frame)

    if cv.waitKey(2) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()