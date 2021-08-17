import cv2
import numpy as np
class ImgPreprocessing:
	def __init__(self,image,kernel):
		self.image=image
		self.kernel=kernel

	#(이미지 가로+필터 가로 -1) 제로프레임을 더해주면됨
	def Conv2D(self):
		fx,fy=np.shape(self.kernel)
		mx,my=np.shape(self.image)
		
		#zeroframe
		zeroframe=np.zeros((fx+mx-1,fy+my-1),dtype=np.int16)
		zx,zy=zeroframe.shape

		#상,하,좌,우 0을 넣어야 되는 크기
		space=(zx-mx)//2

		#이미지에 제로프레임을 추가
		zeroframe[space:space+mx,space:space+my]=self.image[:,:]

		#합성곱
		result=[]
		for i in range(mx):
			for j in range(my):
				result.append((zeroframe[i:i+fx,j:j+fy]*self.kernel).sum())

		result=np.array(result).reshape(mx,my)
		
		return result

kernel=[]
n=int(input("필터의 크기를 입력하시오."))
for i in range(n):
	kernel.append(list(map(int,input().split())))	
image=cv2.imread("cafe.jpg",cv2.IMREAD_GRAYSCALE)
img=ImgPreprocessing(image,kernel)
image=img.Conv2D()
cv2.imwrite("cafe_Convolution"+ str(n) +".jpg",image)

		


