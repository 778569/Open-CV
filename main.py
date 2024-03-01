import numpy as np
import cv2

color = cv2.imread("butterfly.jpg",1)

cv2.imshow("Image",color)
cv2.moveWindow("Image",0,0)
print(color.shape)

height,width,channels = color.shape #356 pixels tall and 493 wide and has 3 color channel
b,g,r =cv2.split(color)#Split to indivitual colors

#create uninitalize array matrixs
#why use "uint8" will be values from 0 to 255 in total
rgb_split = np.empty([height,width*3,3],'uint8')

rgb_split[:,0:width] = cv2.merge([b,b,b])
rgb_split[:,width:width*2] = cv2.merge([g,g,g])
rgb_split[:,width*2:width*3] = cv2.merge([r,r,r])

cv2.imshow("Channels",rgb_split)
cv2.moveWindow("Channels",0,height)

hsv = cv2.cvtColor(color,cv2.COLOR_RGB2HSV)
h,s,v = cv2.split(hsv)
hsv_split = np.concatenate((h,s,v),axis=1)
cv2.imshow("HSV",hsv_split)

cv2.waitKeyEx(0)
cv2.destroyAllWindows()
