## Changing perspective of an image

import cv2 as cv
import numpy as np

img = cv.imread('resources/image-1.jpg')

# Co-ordinate finding fuction
def find_coord(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        print("{} {}".format(x, y)) # left mouse click 
        # defining or printing on the same image or window 
        font = cv.FONT_HERSHEY_PLAIN
        cv.putText(img, "{} {}".format(x, y), (x, y), font, 1, (255, 0, 179), thickness=2)
        cv.imshow("Image", img)

    # for color finding
    if event == cv.EVENT_RBUTTONDOWN:
        print("{} {}".format(x, y)) # left mouse click 
        font = cv.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]

        cv.putText(img, "{} {} {}".format(b, g, r), (x, y), font, 1, (255, 0, 0), 2)
        cv.imshow("Image", img)


# Function to read and display
if __name__ == "__main__":
    img = cv.imread('resources/image-1.jpg', 1)
    cv.imshow("Image", img)
    # set call back function
    cv.setMouseCallback("Image", find_coord)
    cv.waitKey(0)
    cv.destroyAllWindows 



