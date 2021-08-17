import numpy as np
import cv2
import json

class MakeDataset:
    def __init__(self,JsonName,image):
        self.JsonName=JsonName
        self.image=image

    def getMask(self):
        with open(self.JsonName) as jsonFile:
            Objects=json.load(jsonFile)
        
        imgH=Objects['imageHeight'] #1280
        imgW=Objects['imageWidth'] #960
        
        for idx in range(len(Objects['shapes'])):
            point=Objects['shapes'][idx]['points']
            mask=np.zeros((imgH,imgW,1))
            point=Objects['shapes'][0]['points']
            point=np.array(point,np.int32)
            mask=cv2.fillConvexPoly(mask,point,255)

            axis=np.where(mask==255)
            mask_dataset=np.zeros((160,160,100),dtype=np.uint8)
            image_dataset=np.zeros((160,160,3,100),dtype=np.uint8)
            for i in range(100):
                x=axis[0][i*30]
                y=axis[1][i*30]
                mask_dataset[:,:,i]=mask[x-80:x+80,y-80:y+80,0]
                image_dataset[:,:,:,i]=self.image[x-80:x+80,y-80:y+80,:]
            np.save("mask_dataset",mask_dataset)
            np.save("image_dataset",image_dataset)

            
image=cv2.imread("cafe.jpg")
d=MakeDataset('cafe.json',image)
d.getMask()