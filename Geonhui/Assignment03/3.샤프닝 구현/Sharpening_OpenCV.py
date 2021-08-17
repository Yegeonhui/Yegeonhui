import cv2
import numpy as np
image=cv2.imread("cafe.jpg")
sharpening_1=np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
sharpening_2=np.array([[-1, -1, -1, -1, -1],
                         [-1, 2, 2, 2, -1],
                         [-1, 2, 9, 2, -1],
                         [-1, 2, 2, 2, -1],
                         [-1, -1, -1, -1, -1]])/9.0

s_1=cv2.filter2D(image,-1,sharpening_1)
s_2=cv2.filter2D(image,-1,sharpening_2)
merged=np.hstack((image,s_1,s_2))
cv2.imshow("Sharpening",merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
