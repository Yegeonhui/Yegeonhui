import cv2
import numpy as np
class ImgPreprocessing:
	def __init__(self,image,kernel,n):
		self.image=image
		self.kernel=kernel
		self.n=n
	
	def sharpening(self):
    	#블러처리
		blur=cv2.filter2D(self.image,-1,self.kernel) 
		
		#원본이미지-블러이미지=원본이미지가 얼마만큼 변경이 되었나. 
		#차이가 크면 근처 픽셀에 비해 블러링이 많이 이루어진 엣지부분
		g_image=self.image-blur

		#원본이미지+가중치*원본이미지에 비해 변경된 요소
		image=self.image+self.n*g_image
		return image

image=cv2.imread("cafe.jpg")
kernel=np.ones((5,5),dtype=np.int8)/5**2
n=int(input("샤프닝을 어느정도로 할까요?"))
Sharpe=ImgPreprocessing(image,kernel,n)
image=Sharpe.sharpening()
cv2.imshow("cafe_sharpening",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


