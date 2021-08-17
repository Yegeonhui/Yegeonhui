import cv2
import random
nOutput=int(input("몇개를 출력할까요?"))
for k in range(nOutput):
	#1.회전, 2.확대/축소, 3.채도
	degree=random.uniform(0,360)
	scale=random.uniform(0,2)
	saturation=random.uniform(0,255)
	#이미지 불러오기 
	image=cv2.imread("cafe.jpg")

	#1.회전 
	#높이,너비를 이용하여 회전 중심점을 설정
	#2*3 회전 행렬 생성 함수(cv2.getRotationMatrix2D)
	#cv2.getRotationMatrix2D(중심점,각도,비율)
	height,width,channel=image.shape
	matrix=cv2.getRotationMatrix2D((width/2,height/2),degree,scale)

	#cv2.warpAffine(원본이미지, 어파인 맵 행렬, 출력 이미지 크기)
	image=cv2.warpAffine(image,matrix,(width,height))

	#3.채도변경
	#h(hue색상),s(saturation채도),v(value명도)
	#s는 0(무채색)~255(검은색)
	hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
	h,s,v=cv2.split(hsv)
	cv2.add(s,saturation)
	image=cv2.merge((h,s,v))
	image=cv2.cvtColor(image,cv2.COLOR_HSV2BGR)

	cv2.imshow("cafe",image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	cv2.imwrite("cafe "+ str(k) +".jpg",image)


