# Detecting Specific Colors inside python

import cv2 as cv
import numpy as np

img = cv.imread('resources/image-1.jpg') 

# Convert ot HSV - (Hue, Value Saturation)
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Sliders
def slider():
    pass

path = "resources/image-1.jpg"
cv.namedWindow("Bars")
cv.resizeWindow("Bars", 640, 300)

cv.createTrackbar("Hue Minimun", "Bars", 0, 179, slider)
cv.createTrackbar("Hue Maximum", "Bars", 179, 179, slider)

cv.createTrackbar("Value Minimun", "Bars", 0, 179, slider)
cv.createTrackbar("Value Maximum", "Bars", 179, 179, slider)

cv.createTrackbar("Saturation Minimun", "Bars", 0, 179, slider)
cv.createTrackbar("Saturation Maximum", "Bars", 179, 179, slider)

cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()