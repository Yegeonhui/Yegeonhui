from Morphology import Morph
import cv2
import numpy as np
image=cv2.imread("ygh.png")

#3*3 사각형 필터 생성
kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))

#인스턴스 생성
morph=Morph(kernel)

#팽창
dil=morph.dilate(image)
merge=np.hstack((image,dil))
cv2.imshow("dilate_image",merge)
cv2.waitKey(0)
cv2.destroyAllWindows()

#침식
ero=morph.erosion(image)
merge=np.hstack((image,ero))
cv2.imshow("erosion_image",merge)
cv2.waitKey(0)
cv2.destroyAllWindows()

#열린
opening=morph.open(image)
merge=np.hstack((image,opening))
cv2.imshow("open_image",merge)
cv2.waitKey(0)
cv2.destroyAllWindows()

#닫힌
closing=morph.close(image)
merge=np.hstack((image,closing))
cv2.imshow("close_image",merge)
cv2.waitKey(0)
cv2.destroyAllWindows()

#그라디언트
gradient=morph.gradient(image)
merge=np.hstack((image,gradient))
cv2.imshow("gradient_image",merge)
cv2.waitKey(0)
cv2.destroyAllWindows()
