## Saving Manipulated Video

import cv2 as cv

vid = cv.VideoCapture('resources/video.mp4')

# writing format, codec, video writer object and file output
frame_width = int(vid.get(3))
frame_height = int(vid.get(4))

out = cv.VideoWriter("resources/out_video.avi", cv.VideoWriter_fourcc('M', 'j', 'P', 'G'), 30, (frame_width, frame_height), isColor =  False) 

while True:
    ret, frame = vid.read()
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    if ret == True:
        out.write(gray_frame)
        cv.imshow("Video", gray_frame)
        # to quite with 'q'
        if cv.waitKey(2) & 0xFF == ord('q'):
            break
    else:
        break
    
vid.release()
out.release()
cv.destroyAllWindows()