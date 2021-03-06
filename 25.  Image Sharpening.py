# Image Sharpening

import cv2
import numpy as np

img = cv2.imread('C:/Users/kamra/OpenCV/Images/lena.jpg')
cv2.imshow('Original Image', img)
cv2.waitKey(0)


# create sharpening kernel , we don't normalize since values in matrix sum to 1

kernel_sharpening = np.array([[-1,-1,-1],
                              [-1,9,-1],
                              [-1,-1,-1]])

# applying different kernel to the different image 
sharpened = cv2.filter2D(img, -1, kernel_sharpening)

cv2.imshow('Image sharpening', sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()