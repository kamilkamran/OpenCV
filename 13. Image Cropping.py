# Image Cropping

import cv2
import numpy as np

img = cv2.imread("C:/Users/kamra/OpenCV/Images/lena.jpg")

height, width = img.shape[:2]

# lets get staring pixel coordinates (top left, of cropping rectangle)
start_row , start_col  = int(height*.25), int(width*.25)


# lets get staring pixel coordinates (top left, of cropping rectangle)
end_row, end_col = int(height*.75), int(width*.75)

# simply use the indexing to crop the image

cropped = img[start_row:end_row, start_col:end_col]

cv2.imshow('Original Image', img)
cv2.waitKey(0)

cv2.imshow('Cropped Image', cropped)
cv2.waitKey(0)

cv2.destroyAllWindows()