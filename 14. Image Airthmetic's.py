# Image Airthmetic's

import cv2
import numpy as np

img = cv2.imread("C:/Users/kamra/OpenCV/Images/lena.jpg")

cv2.imshow('Originl Image', img)
cv2.waitKey(0)
#M = np.ones(img.shape, dtype="uint8") * 150
M = np.zeros(img.shape, dtype="uint8") + 150


added = cv2.add(img, M)
cv2.imshow('Added', added)

subtracted = cv2.subtract(img, M)
cv2.imshow('MUL', subtracted)

mul = cv2.multiply(img, M)
cv2.imshow('MUL', mul)

cv2.waitKey(0)
cv2.destroyAllWindows()

