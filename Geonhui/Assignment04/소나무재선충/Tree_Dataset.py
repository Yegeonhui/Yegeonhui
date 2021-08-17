import numpy as np
import cv2
import json

class MakeDataset:
    def __init__(self, JsonName, dataset):
        self.JsonName = JsonName
        self.dataset=dataset

    def getMask(self):
        with open(self.JsonName) as jsonFile:
            Objects = json.load(jsonFile)

        imgH = Objects['imageHeight'] #5000
        imgW = Objects['imageWidth'] #5000

        if len(Objects['shapes']) == 1:
            mask = np.zeros((imgH, imgW, 1)) #0=어두움 
            point = Objects['shapes'][0]['points']
            point = np.array(point, np.int32)    
            mask = cv2.fillConvexPoly(mask, point, 255) #255 하얀색
            #마스크에서 값이 255인 x,y좌표를 뽑아냄
            #2차행렬로 나옴 [[x],[y],[c]]
            #axis[0:x 1:y 2:c][좌표개수]

            axis=np.where(mask==255)
            image=cv2.imread("1.tif")
            #l=len(axis[0]) #흰색 픽셀의 갯수 1499
            mask_dataset=np.zeros((224,224,self.dataset),dtype=np.uint8)
            image_dataset=np.zeros((224,224,3,self.dataset),dtype=np.uint8)
            for n in range(self.dataset):                                                                                              
                try:
                    x=axis[0][n*30] #x좌표 30개 마다 뽑기 
                    y=axis[1][n*30] #y좌표 30개 마다 뽑기
                except:
                    pass
                 #if 0<=x-112 and x+112<imgW and 0<=y-112 and y+112<imgH:
                mask_dataset[:,:,n]=mask[x-112:x+112,y-112:y+112,0]
                image_dataset[:,:,:,n]=image[x-112:x+112,y-112:y+112,:]
            np.save("mask_dataset",mask_dataset)
            np.save("image_dataset",image_dataset)
            
            
        elif len(Objects['shapes']) > 1:
            mask = np.zeros((imgH, imgW, 1))
            for idx in range(len(Objects['shapes'])):
                point = Objects['shapes'][idx]['points']
                point = np.array(point, np.int32)
                mask = cv2.fillConvexPoly(mask, point, 255)
                #마스크에서 값이 255인 x,y좌표를 뽑아냄
                #2차행렬로 나옴 [[x],[y],[c]]
                #axis[0:x 1:y 2:c][좌표개수]
    
                axis=np.where(mask==255)

                image=cv2.imread("1.tif")
                mask_dataset=np.zeros((224,224,self.dataset),dtype=np.uint8)
                image_dataset=np.zeros((224,224,3,self.dataset),dtype=np.uint8)
                for n in range(self.dataset):
                    try:
                        x=axis[0][n*30] #x좌표 30개 마다 뽑기  
                        y=axis[1][n*30] #y좌표 30개 마다 뽑기
                    except:
                        pass
                    mask_dataset[:,:,n]=mask[x-112:x+112,y-112:y+112,0]
                    image_dataset[:,:,:,n]=image[x-112:x+112,y-112:y+112,:] 
                np.save("mask_datset"+ str(idx),mask_dataset)
                np.save("image_dataset" + str(idx),image_dataset)
        
        return mask

    def saveMask(self):
        mask = self.getMask()

        maskName = self.JsonName[:-5] + '.jpg'

        cv2.imwrite(maskName, mask)

n=int(input("몇개를 하나의 데이터셋으로 만들까요?"))
mask=MakeDataset("2.json",n)
mask.getMask()