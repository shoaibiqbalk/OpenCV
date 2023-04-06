# Reading a video

import cv2 as cv

vid = cv.VideoCapture('resources/video.mp4')

# Indicator
if vid.isOpened() == False:
    print("Error in reading video")

# Reading and playing

while vid.isOpened():
    ret, frame = vid.read()
    if ret == True:
        cv.imshow("Video", frame)
        if cv.waitKey(2) & 0xFF == ord('q'):
            break
    else:
        break
    
vid.release()
cv.destroyAllWindows()