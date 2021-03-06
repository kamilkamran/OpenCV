# Read Image

import cv2

img = cv2.imread('C:/Users/kamra/OpenCV/Images/lena.jpg')
cv2.imshow('Output Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

