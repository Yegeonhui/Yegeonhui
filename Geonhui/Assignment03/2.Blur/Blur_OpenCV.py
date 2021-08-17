import cv2
import numpy as np
image=cv2.imread("cafe.jpg")
blur1=cv2.blur(image,(10,10))
blur2=cv2.boxFilter(image,-1,(10,10))
merged=np.hstack((image,blur1,blur2))

#gaussian=cv2.GaussianBlur(image,(5,5),0)
#cv2.imshow("gaussian_blur",gaussian)
cv2.imshow("blur",merged)
cv2.waitKey(0)
cv2.destroyAllWindows