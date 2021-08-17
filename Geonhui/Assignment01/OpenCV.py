#추가
import cv2
image=cv2.imread("cafe.jpg")
print("픽셀수",image.shape) #이미지의 픽셀수 
print("사이즈",image.size) #이미지의 사이즈
px=image[100,100]
print("100*100픽셀",px) #이미지의 100*100의 픽셀
print("100*100픽셀의 B값",px[0]) #100*100 픽셀의 B값
image[50:500,50:500,0]=0 #이미지의 가로 50~500, 세로 50~500까지 B의 값을 0으로 세팅
cv2.imshow("cafe_cng",image)
cv2.waitKey(0)
cv2.destroyAllWindows

