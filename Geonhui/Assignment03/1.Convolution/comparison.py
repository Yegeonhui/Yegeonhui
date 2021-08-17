import cv2
import numpy as np
cafe_for=cv2.imread("cafe_Convolution5.jpg")
cafe_opencv=cv2.imread("cafe_opencv.jpg")
merged=np.hstack((cafe_for,cafe_opencv))
cv2.imshow("comparsion",merged)
cv2.waitKey(0)
cv2.destroyAllWindows()