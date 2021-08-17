#평균블러링
import cv2
import numpy as np
image=cv2.imread("cafe.jpg")
n=int(input("강도는 어느정도..?"))
kernel=np.ones((n,n))/n**2
image=cv2.filter2D(image,-1,kernel)
cv2.imshow("cafe_blur",image)
cv2.waitKey(0)
cv2.destroyAllWindows


