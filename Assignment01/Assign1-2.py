#image=cv2.imread("cafe.jpg",cv2.IMREAD_UNCHANGED)
#1-2. Python OpenCV에서 이미지를 불러와서 색상 변경시켜보기
import cv2
#이미지를 변수로 불러오기
#image=cv2.imread("cafe.jpg",cv2.IMREAD_GRAYSCALE) 
#image=cv2.imread("cafe.jpg",cv2.IMREAD_UNCHANGED)
image=cv2.imread("cafe.jpg")

#이미지보기
cv2.imshow("cafe",image) 
cv2.waitKey(0) #아무입력이나 들어오기 전까지 대기, 0이 기본
cv2.destroyAllWindows #활성화되어 있는 모든 윈도우 창 종료

#이미지 색상 변경
image[:,:,0]=0 #2번째 index 0은 B, 1은 G, 2는 R를 의미함.
cv2.imwrite("cafe_Blue.jpg",image) #색변경한 이미지를 저장
 
cv2.imshow("cafe_Blue",image) #변경된 이미지를 다시보기
cv2.waitKey(0) #아무입력이나 들어오기 전까지 대기, 0이 기본
cv2.destroyAllWindows() #활성화되어 있는 모든 윈도우 창 종료



