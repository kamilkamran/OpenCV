# Image Rotation

import cv2
import numpy as np

img = cv2.imread("C:/Users/kamra/OpenCV/Images/lena.jpg")

height, width = img.shape[:2]

rotation_matric = cv2.getRotationMatrix2D((width/4, height/4), 70, .8)

rotated_img = cv2.warpAffine(img, rotation_matric, (width, height))

cv2.imshow('Rotated Image', rotated_img)
cv2.imshow('Original Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()