import cv2
import numpy as np
class Morph:
	#생성자
	def __init__(self,kernel):
		self.kernel=kernel

	#팽창
	#검정색 노이즈 제거 
	def dilate(self,image):
		dil=cv2.dilate(image,self.kernel)
		return dil
		
	#침식
	#노이즈 제거 효과 떨어져 있는 물체
	def erosion(self,image):
		ero=cv2.erode(image,self.kernel)
		return ero
	
	#열린(침식->팽창)
	#주변보다 밝은 노이즈를 제거 
	def open(self,image):
		image1=self.erosion(image)
		opening=self.dilate(image1)
		return opening 

	#닫힌(팽창->침식)
	#어두운 노이즈를 제거, 구멍을 메우는데 효과 
	def close(self,image):
		image1=self.dilate(image)
		closing=self.erosion(image1)
		return closing

	#그레디언트(팽창-침식)
	#경계선
	def gradient(self,image):
		dilate=self.dilate(image)
		erosion=self.erosion(image)
		gradient=dilate-erosion
		return gradient