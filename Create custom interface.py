
# in here drawing a circle onto the screen and place the circle base on whatever we have last clicked
import numpy as np
import cv2

#Request to, the operating system using the camera

cap = cv2.VideoCapture(0) # Specify 0 input
# In here operatignsystem and opencv do in order to decide what camera to use if there are multiple. and how to handle passing frames into OpenCv


color =(0,255,0)
line_width = 3 # line thisckness
radius = 100 # radius of the circle
point = (0,0) # initial point

#To capture mouse click  we create a function

def click(event,x,y,flages,param):
#variables are global
    global point, pressed # this is the call back everytime click the mouse on the video feed
    if event ==cv2.EVENT_LBUTTONDOWN:
        print("Pressed", x,y)
        point(x,y) # every time we click left button down it will set the point

#regiter with this event with open cv handler
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame",click)
#If we put Left button up popint at lifting up
#Crwate a while loop mean for the video feed
while(True):

    #read from the video capture
    ret, frame = cap.read() # this always read new from the video capture.

    #Resize the imageq
    frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    cv2.circle(frame,point,radius,color,line_width)
    cv2.imshow("Frame",frame)
    #register await key
    #because if we dont register a legitimate exit to our loop, then getting stuck, not out fo the application
    ch= cv2.waitKey(1)
    #this mean run every one millisecond
    #if you want to out the video press "q"
    if ch & 0xFF == ord('q'):
        break

#end of program we use cap.release()
cap.release()
cv2.destroyAllWindows()
