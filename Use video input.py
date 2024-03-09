import numpy as np
import cv2

#Request to, the operating system using the camera

cap = cv2.VideoCapture(0) # Specify 0 input
# In here operatignsystem and opencv do in order to decide what camera to use if there are multiple. and how to handle passing frames into OpenCv

#Crwate a while loop mean for the video feed
while(True):

    #read from the video capture
    ret, frame = cap.read() # this always read new from the video capture.

    #Resize the imageq
    frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    cv2.imshow("Frame",frame)
    #register await key
    #because if we dont register a legitimate exit to our loop, then getting stuck, not out fo the application
    ch= cv2.waitKey(1);
    #this mean run every one millisecond
    #if you want to out the video press "q"
    if ch & 0xFF == ord('q'):
        break

#end of program we use cap.release()
cap.release()
cv2.destroyAllWindows()
