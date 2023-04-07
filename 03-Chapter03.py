## Basic Manipulation of Images

import cv2 as cv
import numpy as np

img = cv.imread('resources/image-1.jpg')

# Resizing
img = cv.resize(img, (800, 600))

# Grayscale
gray_img =  cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Blurred Image
blurr_img = cv.GaussianBlur(img, (7, 7), 0)

# Edge Detection
edge_img = cv.Canny(img, 48, 48)

# Dilated Image - Thickness of edge lines
mat_kernal = np.ones((7, 7), np.uint8)
dilated_img = cv.dilate(edge_img, (mat_kernal), iterations=1)

# Eroded Image - Thinnes of edge lines
ero_img = cv.erode(edge_img, mat_kernal, iterations=1)


cv.imshow('First Image', img)
cv.imshow('Gray Image', gray_img)
cv.imshow('Blurred Image', blurr_img)
cv.imshow('Edge Image', edge_img)
cv.imshow('Dilated Image', dilated_img)
cv.imshow('Eroded Image', ero_img)


cv.waitKey(0)
cv.destroyAllWindows()