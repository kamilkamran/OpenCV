# Convert RGB to Gray Image

import cv2

img = cv2.imread('C:/Users/kamra/OpenCV/Images/lena.jpg')
# img = cv2.imread('C:/Users/kamra/OpenCV/Images/lena.jpg',0)

cv2.imshow('Original Image', img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray Image', gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()


