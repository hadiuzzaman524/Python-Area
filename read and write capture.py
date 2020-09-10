import cv2

cap=cv2.VideoCapture(0)

#for saving video
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
#for learn fourcc code visit www.fourcc.org/codecs.php
#0 means which camera can work 1st or 2nd or anything
#the video writer parameter is output file name,fourcc code,number of frame per second and (height,width)


while (cap.isOpened()):
    #cap.isOpened() method check if camera
    #will work or not
    ret, frame=cap.read()
    # return a capture and store in frame variable
    if ret==True:

        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # print frame height and width..

        out.write(frame)
        # for saving file

        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # in the capture frame variable color chenge using this line
        cv2.imshow('frame',gray)
        # set the chenge color in frame

        if cv2.waitKey(1) & 0xff== ord('q'):
        #check waitkey() using for wait user input  and 0xff means 64bit machine
        # and ord('q') means if user press q
            break
cap.release()
#after capture it must be release
out.release()
#release because out help us to save capture
cv2.destroyAllWindows()
#for destroy all window when exit program