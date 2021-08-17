import cv2
import numpy as np

#팽창
image=cv2.imread("ygh.png")
k=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
dil=cv2.dilate(image,k)
merged=np.hstack((image,dil))
cv2.imshow("dilate",merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

#침식
image=cv2.imread("Geonhui/Assignment03/ygh.png")
k=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
erosion=cv2.erode(image,k)
merged=np.hstack((image,erosion))
cv2.imshow("Erode",merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

#열린
image=cv2.imread("Geonhui/Assignment03/ygh.png")
k=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
erosion=cv2.erode(image,k)
opening=cv2.dilate(erosion,k)
merged=np.hstack((image,opening))
cv2.imshow("opening",merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

#닫힌
image=cv2.imread("Geonhui/Assignment03/ygh.png")
k=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
dilate=cv2.dilate(image,k)
closing=cv2.erode(dilate,k)
merged=np.hstack((image,closing))
cv2.imshow("closing",merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

#그레디언트
image=cv2.imread("Geonhui/Assignment03/ygh1.png")
k=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
dilate=cv2.dilate(image,k) 
erosion=cv2.erode(image,k)
gradient=dilate-erosion
merged=np.hstack((image,gradient))
cv2.imshow("gradient",merged)
cv2.waitKey(0)
cv2.destroyAllWindows()