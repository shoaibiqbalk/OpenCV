# Detecting Specific Colors inside python

import cv2 as cv
import numpy as np

img = cv.imread('resources/image-1.jpg') 
img = cv.resize(img, (800, 600))

# Convert ot HSV - (Hue, Value Saturation)
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Sliders
def slider():
    pass

path = "resources/image-1.jpg"

 
cv.namedWindow("Bars")
cv.resizeWindow("Bars", 640, 300)

cv.createTrackbar("Hue Min", "Bars", 0, 179, slider)
cv.createTrackbar("Hue Max", "Bars", 179, 179, slider)

cv.createTrackbar("Sat Min", "Bars", 0, 255, slider)
cv.createTrackbar("Sat Max", "Bars", 255, 255, slider)

cv.createTrackbar("Val Min", "Bars", 0, 255, slider)
cv.createTrackbar("Val Max", "Bars", 255, 255, slider)


while True:
    img = cv.imread(path)
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    hue_min = cv.createTrackbar("Hue Min", "Bars", 0, 179, slider)
    hue_max = cv.createTrackbar("Hue Max", "Bars", 179, 179, slider)

    sat_min = cv.createTrackbar("Sat Min", "Bars", 0, 255, slider)
    sat_max =cv.createTrackbar("Sat Max", "Bars", 255, 255, slider)

    val_min = cv.createTrackbar("Val Min", "Bars", 0, 255, slider)
    val_max = cv.createTrackbar("Val Max", "Bars", 255, 255, slider)

    print(hue_min, hue_max, sat_min, sat_max, val_min, val_max)

    # changes inside an image
    lower = np.array([hue_min, sat_min, val_min])
    lower = np.array([hue_max, sat_max, val_max])     

    cv.imshow('Image', img)
    cv.imshow('HSV Image', hsv_img)
    if cv.waitKey(2) & 0xFF == ord('q'):
            break

cv.destroyAllWindows()