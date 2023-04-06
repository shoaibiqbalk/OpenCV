# Reading a video

import cv2 as cv

vid = cv.VideoCapture('resource/video.mp4')

if vid.isOpened() == False:
    print("Error in reading video")

    