## Converting into Grayscale

# library import
import cv2 as cv
from cv2 import cvtColor

img = cv.imread('resources/image-1.jpg')
img = cv.resize(img, (800, 600))

