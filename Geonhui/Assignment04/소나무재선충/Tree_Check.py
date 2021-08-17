import numpy as np
import cv2
image_dataset=np.load("image_dataset.npy")
mask_dataset=np.load("mask_dataset.npy")

#image=cv2.imread("2.jpg")
#print(np.where(image==[255,255,255]))
#image=cv2.imread("2.jpg",cv2.IMREAD_GRAYSCALE)      
#print(image)
#print(np.where(image==255))

for i in range(10):
    image=image_dataset[:,:,:,i] 
    mask=mask_dataset[:,:,i]
    cv2.imshow("mask",mask)
    cv2.imshow("image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()            