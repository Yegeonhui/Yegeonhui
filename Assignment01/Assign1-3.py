#1-3. Python OpenCV에서 이미지의 색공간을 변경시켜보기
import cv2
#'cafe.jpg'라는 이미지를 image라는 변수로 저장 
image=cv2.imread("Geonhui/cafe.jpg") 
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV) #hsv컬러로 변경   
lab=cv2.cvtColor(image,cv2.COLOR_BGR2LAB) #lab컬러로 변경
grayscale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #grayscalse컬러로 변경

cv2.imshow("hsv",hsv) #hsv컬러로 보기 
cv2.waitKey(0) #아무입력이나 들어오기 전까지 대기, 0이 기본
cv2.destroyAllWindows() #활성화되어 있는 모든 윈도우 창 종료

cv2.imshow("lab",lab)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("grayscale",grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()
