# Template Matching (Object Detection) 

import numpy as np
import cv2 as cv

img = cv.resize(cv.imread('resources/soccer_practice.jpg', 0), (0, 0), fx=0.8, fy=0.8)
template = cv.resize(cv.imread('resources/ball.PNG', 0), (0, 0), fx=0.8, fy=0.8)
h, w = template.shape
methods = [cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED, cv.TM_CCORR,
            cv.TM_CCORR_NORMED, cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()

    result = cv.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)    
    cv.rectangle(img2, location, bottom_right, 255, 5)
    cv.imshow('Match', img2)
    cv.waitKey(0)
    cv.destroyAllWindows()