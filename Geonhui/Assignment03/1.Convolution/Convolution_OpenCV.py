import cv2
import numpy as np
image=cv2.imread("cafe.jpg",cv2.IMREAD_GRAYSCALE)
kernel=[]    
n=int(input("필터의 크기를 입력하시오."))
for i in range(n):
	kernel.append(list(map(int,input().split())))
kernel=np.array(kernel,dtype=np.int16)
image=cv2.filter2D(image,-1,kernel)
cv2.imwrite("cafe_opencv.jpg",image)