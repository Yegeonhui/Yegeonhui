import cv2
class ImgAug:
	def __init__(self,degree,scale,sat):
		#각도, 비율, 채도를 초기화 함수로 받음. 
		self.degree=degree
		self.scale=scale
		self.sat=sat

	#회전,크기 변경하는 함수
	def rotate(self,image):
		height,width,channel=image.shape
		#2*3 회전 행렬 생성 함수를 사용해서 
		#회전변환 행렬을 만들어준다.
		matrix=cv2.getRotationMatrix2D((width/2,height/2),self.degree,self.scale)
		
		#어파인 변환함수로 회전 변환을 계산한다.
		#cv2.warpAffine(원본이미지, 어파인 맵 행렬, 출력 이미지 크기)
		image=cv2.warpAffine(image,matrix,(width,height))
		return image

	#채도 변경하는 함수 
	def saturation(self,image):
		hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
		h,s,v=cv2.split(hsv)
		#이미지의 채도에 랜덤함수로 뽑아낸 saturation을 일괄적으로 더해줌
		s=cv2.add(s,self.sat)
		image=cv2.merge((h,s,v))
		image=cv2.cvtColor(image,cv2.COLOR_HSV2BGR)
		return image

		
		


		
