## Spliting video into frames

import cv2 as cv

vid = cv.VideoCapture("resources/video.mp4")

frameNr = 0

while True:
    success, frame = vid.read()
    if success:
        