# Image resizing using pyramid

import cv2
import numpy as np

img = cv2.imread("C:/Users/kamra/OpenCV/Images/lena.jpg")

smaller = cv2.pyrDown(img)
larger = cv2.pyrUp(img)

cv2.imshow('Original Image', img)
cv2.imshow('Smaller Image', smaller)
cv2.imshow('Larger Image', larger)

cv2.waitKey(0)
cv2.destroyAllWindows()