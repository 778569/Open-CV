import cv2

color = cv2.imread("butterfly.jpg")

gray = cv2.cvtColor(color,cv2.COLOR_RGB2GRAY)
cv2.imwrite("gray.jpg",gray)
cv2.imshow("gray", gray)

# grab the individual chnanel for the image

b = color[:,:,0]
g = color[:,:,1]
r = color[:,:,2]

rgba = cv2.merge((b,g,r,g))
cv2.imwrite("rgba.png",rgba)

cv2.imshow("rgba", rgba)

cv2.waitKeyEx(0)
cv2.destroyAllWindows()

