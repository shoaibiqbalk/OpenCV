## Saving an Image

# library import
import cv2 as cv
from cv2 import cvtColor
from cv2 import imwrite

img = cv.imread('resources/image-1.jpg')
img = cv.resize(img, (800, 600))

gray_img =  cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', gray_img)
imwrite('resources/image_gray.png', gray_img)

cv.waitKey(0)
cv.destroyAllWindows()