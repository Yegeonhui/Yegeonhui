import numpy as np
import cv2
from glob import glob
import os

class galaxy:
    def __init__(self,w,h,criteria,objp,images,distortion_img):
        self.w=w
        self.h=h
        self.criteria=criteria
        self.objp=objp
        self.images=images
        self.distortion_img=distortion_img
        #obj: 3차원 점 #imgpoints:2차원점 
        self.objpoints=[]
        self.imgpoints=[]

    def getmatrix(self):
        for image in self.images:
            img=cv2.imread(image)
            img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            #ret: True,False / corners: 좌표
            ret,corners=cv2.findChessboardCorners(img_gray,(self.w,self.h),None)
            print(ret)
            if ret:
                self.objpoints.append(self.objp)
                #최대의 정확도로 모서리를 찾아줌
                corners2=cv2.cornerSubPix(img_gray,corners,(11,11),(-1,-1),self.criteria)
                self.imgpoints.append(corners2)
                cv2.drawChessboardCorners(img,(self.w,self.h),corners2,ret)
                # img1=cv2.resize(img,dsize=(640,480),interpolation=cv2.INTER_AREA)
                # cv2.imshow("img",img1)
                # cv2.waitKey(0)
               
        #카메라내부파라미터, 왜곡계수, 회전, 이동벡터변환
        self.ret,self.mtx,self.dist,rvecs,tvecs=cv2.calibrateCamera(self.objpoints,self.imgpoints,img_gray.shape[::-1],None,None)
        print(self.mtx)

    def undistortion(self):
        img=cv2.imread(self.distortion_img)
        height,width=img.shape[:2]
        #카메라 메트릭스 개선 / 스케일링 인자 alpha=0일 경우, 원치않는 픽셀                                      
        newcameramtx,roi=cv2.getOptimalNewCameraMatrix(self.mtx,self.dist,(width,height),1)
        dst=cv2.undistort(img,self.mtx,self.dist,None,newcameramtx)
        x,y,w,h=roi
        dst=dst[y:y+h,x:x+w]
        cv2.imwrite("correction.jpg",dst)
        

#h,w=int(input("격자 가로세로(세로:h, 가로:w)"))
w=9
h=7
criteria=(cv2.TERM_CRITERIA_EPS+cv2.TermCriteria_MAX_ITER,30,0.001)
objp=np.zeros((w*h,3),np.float32)
objp[:,:2]=np.mgrid[0:w,0:h].T.reshape(-1,2)

#불러올 체스판  
route=os.getcwd()
route_chess=route+"/galaxy"
images=glob(route_chess+"/*.jpg")

#왜곡된 이미지
distortion_img=route+"/red.jpg"

i=galaxy(w,h,criteria,objp,images,distortion_img)
i.getmatrix()
i.undistortion()


#cd geonhui/assignment05
# #https://blog.naver.com/zeus05100/221731468192

#https://blog.naver.com/jinwoo6612/221825654099
