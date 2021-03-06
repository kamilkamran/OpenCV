# Write an image

import cv2

img = cv2.imread('C:/Users/kamra/OpenCV/Images/lena.jpg')
cv2.imshow('Original Image', img)

cv2.imwrite('Output.jpg', img)
cv2.imwrite('Original Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()