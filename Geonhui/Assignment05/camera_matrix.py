import numpy as np
import cv2
from glob import glob
import os

#criteria : 반복을 종료할 조건(type(종료 조건), 최대 iter, epsilon값(정확도))
# cv2.TERM_CRITERIA_EPS : 주어진 정확도(epsilon 인자)에 도달하면 반복을 중단
# cv2.TERM_CRITERIA_MAX_ITER : max_iter 인자에 지정된 횟수만큼 반복하고 중단
# a + b : 두가지 조건 중 하나가 만족되면 반복 중단
criteria=(cv2.TERM_CRITERIA_EPS+cv2.TermCriteria_MAX_ITER,30,0.001)

objp=np.zeros((9*7,3),np.float32)
objp[:,:2]=np.mgrid[0:9,0:7].T.reshape(-1,2)

objpoints=[]
imgpoints=[]

route=os.getcwd()+"/galaxy"
images=glob(route+"/*.jpg")
for image in images:
    img=cv2.imread(image)
    h,w=img.shape[:2]
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    #체스판의 패턴을 찾아준다. 
    #ret : True,False #corners: 좌표 
    ret,corners=cv2.findChessboardCorners(img_gray,(9,7),None)
    if ret:
        objpoints.append(objp)
        #최대의 정확도로 모서리를 찾아야됨 
        corners2=cv2.cornerSubPix(img_gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)
        #이미지에 점을 찍어줌
        cv2.drawChessboardCorners(img,(9,7),corners2,ret)
        # img2=cv2.resize(img,dsize=(480,480),interpolation=cv2.INTER_AREA)
        # cv2.imshow("img",img2)
        # cv2.waitKey(0)
#메트릭스,왜곡계수,회전/변환벡터 
ret,mtx,dist,rvecs,tvecs=cv2.calibrateCamera(objpoints,imgpoints,img_gray.shape[::-1],None,None)

#ret,카메라 행렬, 왜곡계수, 회전, 이동벡터 변환
# #왜곡제거 
#카메라 메트릭스 개선(alpha=1 모든픽셀 유지)
#roi: 결과를 자르고 사용할수 있는 이미지 roi  
route_img=route+"/1.jpg"
img=cv2.imread(route_img)
h,w=img.shape[:2]
newcameramtx,roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
dst=cv2.undistort(img,mtx,dist,None,newcameramtx)
x,y,w,h=roi
dst=dst[y:y+h,x:x+w]
img2=cv2.resize(dst,dsize=(480,480),interpolation=cv2.INTER_AREA)
cv2.imshow("img",img2)
cv2.imwrite("img.jpg",dst)
cv2.waitKey(0)
cv2.destroyAllWindows


       

