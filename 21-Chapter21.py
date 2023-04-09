## Changing perspective of an image

import cv2 as cv
import numpy as np

img = cv.imread('resources/image-1.jpg')

# Co-ordinate finding fuction
def find_coord(event, x, y, flags, params):
    if event == cv.EVENT_FLAG_LBUTTON:
        print("{} {}".format(x, y)) # left mouse click 
        # defining or printing on the same image or window 
        font = cv.FONT_HERSHEY_PLAIN
        cv.putText(img, "{} {}".format(x, y), (x, y), font, 1, (255, 0, 179), thickness=2)
        cv.imshow("Image", img)


# Function to read and display
if __name__ == "__main__":
    img = cv.imread



