import cv2
import numpy as np
class ImgPreprocessing:
    def __init__(self,image,kernel):
        self.image=image
        self.kernel=kernel

    def Blur(self):
        blur=cv2.filter2D(self.image,-1,self.kernel)
        return blur

n=int(input("어느정도 블러처리를 할까요?"))
kernel=np.ones((n,n),dtype=np.int8)/n**2
image=cv2.imread("cafe.jpg")
blur=ImgPreprocessing(image,kernel)
image=blur.Blur()
cv2.imshow("cafe_blur",image)
cv2.waitKey(0)
cv2.destroyAllWindeows()
