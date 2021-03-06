#Image Blurring Operations

import cv2
import numpy as np

img = cv2.imread("C:/Users/kamra/OpenCV/Images/lena.jpg")
cv2.imshow('Original Image', img)
cv2.waitKey(0)


# creating 3x3 kernel
kernel_3x3 = np.ones((3,3), np.float)/9
# We use the cv2.filter2D to convolve the kernel with Image
blurred1 = cv2.filter2D(img, -1, kernel_3x3)
cv2.imshow('kernel Image', blurred1)
cv2.waitKey(0)



kernel_7x7 = np.ones((7,7), np.float)/49
blurred2 = cv2.filter2D(img, -1, kernel_7x7)
cv2.imshow('kernel Image', blurred2)
cv2.waitKey(0)
cv2.destroyAllWindows()