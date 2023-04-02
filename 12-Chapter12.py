# Corner Detection

import cv2 as cv
import numpy as np

img = cv.imread('resources/chessboard.png')
img = cv.resize(img, (0, 0), fx=0.5, fy=0.5)
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray_img, 100, 0.5, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv.circle(img, (x, y), 5, (255, 0, 0), -1)

for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv.line(img, corner1, corner2, (), 1)

cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()