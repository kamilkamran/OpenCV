# Image Bitwise Operations

import cv2
import numpy as np

square = np.zeros((300,300), np.uint8)

cv2.rectangle(square, (50,50), (250,250), 255, -1)
cv2.imshow("Square", square)
cv2.waitKey(0)

# Making an eclipse
ellipse = np.zeros((300,300), np.uint8)
cv2.ellipse(ellipse, (150,150), (150,150), 30, 0, 180, 255, -1)
cv2.imshow("Ellipse", ellipse)
cv2.waitKey()

And = cv2.bitwise_and(square, ellipse)
cv2.imshow("AND", And)
cv2.waitKey(0)

OR = cv2.bitwise_or(square, ellipse)
cv2.imshow("OR", OR)
cv2.waitKey(0)

Xor = cv2.bitwise_xor(square, ellipse)
cv2.imshow("XOR", Xor)
cv2.waitKey(0)

Not = cv2.bitwise_not(square, ellipse)
cv2.imshow("Not", Not)
cv2.waitKey(0)

cv2.destroyAllWindows()

