# Capture Image Using Webcam

import matplotlib.pyplot as plt
import cv2


cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret, frame = cap.read()
    print(ret)
    print(frame)
    
else:
    ret = False
    
img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

plt.imshow(img1)
plt.title("Camera Image-1") 
plt.xticks([]) 
plt.yticks([])
plt.show()
cap.release() 