# Image Translation

import cv2
import numpy as np

img = cv2.imread("C:/Users/kamra/OpenCV/Images/lena.jpg")

# store height and width of the Image

height, width = img.shape[:2]
print(height)
print(width)

quarter_height, quarter_width = height/2, width/2
print(quarter_height)
print(quarter_width)


#       |1  0  Tx|
#       |0  1  Ty|

# T is our translation matrix

T = np.float32([[1, 0, quarter_width],
                [0, 1, quarter_height]])

print(T)

# we use warpAffine Transformation to shift the Image

img_translation = cv2.warpAffine(img, T, (width, height))
cv2.imshow('Original Image', img)
cv2.imshow('Translation', img_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()