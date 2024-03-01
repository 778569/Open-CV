import numpy as np
import cv2

image = cv2.imread("thresh.jpg")
cv2.imshow("Original",image)

blur = cv2.GaussianBlur(image,(5,55),0)
cv2.imshow("Blur",blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
