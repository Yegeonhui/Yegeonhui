from AssignOOP import ImgAug
import random
import cv2
nOutput=int(input("몇개를 출력할까요?"))
image=cv2.imread("Geonhui/cafe.jpg")
height,width,channel=image.shape
for k in range(nOutput):
    #각도, 비율, 채도
    degree=random.uniform(0,360)
    scale=random.uniform(0,2)
    sat=random.uniform(0,255)
    
    #인스턴스 생성
    img=ImgAug(degree,scale,sat)
    
    #이미지를 변경시켜주는 메서드 실행
    image1=img.rotate(image)
    image2=img.saturation(image1)
    cv2.imwrite("cafe"+str(k)+".jpg",image2)


  