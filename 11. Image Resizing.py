# Image Resizing and interpolation

import cv2
import numpy as np

img = cv2.imread("C:/Users/kamra/OpenCV/Images/lena.jpg")


cv2.imshow('Original Image', img)
cv2.waitKey(0)

img_scaled = cv2.resize(img, None, fx=0.75, fy=0.75)
cv2.imshow('Scaling - Linear Interpolation', img_scaled)
cv2.waitKey(0)


img_scaled1 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Scaling - Cubic Interpolation', img_scaled1)
cv2.waitKey(0)


img_scaled2 = cv2.resize(img, (900, 400), interpolation=cv2.INTER_AREA)
cv2.imshow('Scaling - Skewed', img_scaled2)
cv2.waitKey(0)


cv2.destroyAllWindows()