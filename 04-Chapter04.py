## Converting into Grayscale

# library import
import cv2 as cv
from cv2 import cvtColor

img = cv.imread('resources/image-1.jpg')
img = cv.resize(img, (800, 600))

gray_img =  cvtColor(img, cv.COLOR_BGR2GRAY)

(thresh, b_w) = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)

cv.imshow('First Image', img)
cv.imshow('Gray Image', gray_img)
cv.imshow('Gray Image', b_w)

cv.waitKey(0)
cv.destroyAllWindows()