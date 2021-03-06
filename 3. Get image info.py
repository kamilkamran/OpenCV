# Get image info

import cv2
img = cv2.imread('C:/Users/kamra/OpenCV/Images/lena.jpg')

cv2.imshow('Output Image', img)
print(img.shape)

print("Height pixel value :", img.shape[0])
print("Width pixel value :", img.shape[1])

cv2.waitKey(0)
cv2.destroyAllWindows()