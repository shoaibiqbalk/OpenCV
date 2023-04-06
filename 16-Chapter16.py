## Converting video to grayscale or black & white

import cv2 as cv

vid = cv.VideoCapture('resources/video.mp4')

while True:
    ret, frame = vid.read()
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    if ret == True:
        cv.imshow("Video", gray_frame)
        # to quite with 'q'
        if cv.waitKey(2) & 0xFF == ord('q'):
            break
    else:
        break
    
vid.release()
cv.destroyAllWindows()