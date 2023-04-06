## Saving videos from cam

import cv2 as cv

vid = cv.VideoCapture(0)

# writing format, codec, video writer object and file output
frame_width = int(vid.get(3))
frame_height = int(vid.get(4))

out = cv.VideoWriter("resources/cam_video.avi", cv.VideoWriter_fourcc('M', 'j', 'P', 'G'), 10, (frame_width, frame_height)) 

while True:
    ret, frame = vid.read()
    if ret == True:
        out.write(frame)
        # to quite with 'q'
        if cv.waitKey(2) & 0xFF == ord('q'):
            break
    else:
        break
    
vid.release()
out.release()
cv.destroyAllWindows()