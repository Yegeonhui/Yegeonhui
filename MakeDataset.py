import json
import os
import numpy as np
import cv2
from glob import glob

class MakeMask:
    def __init__(self,route,JsonFile,ImageFile,n):
        self.route=route
        self.JsonFile=JsonFile
        self.ImageFile=ImageFile
        self.n=n

    def Makedir(self,route):
        os.makedirs(route+"/Mask",exist_ok=True)
        os.makedirs(route+"/Image",exist_ok=True)
        

    def getFile(self):
        for File in range(len(self.JsonFile)):
            Json=self.JsonFile[File]
            Image=self.ImageFile[File]
            
            self.getDataset(Json,Image)

    def getDataset(self,Json,Image,PixelSize=112):
        Name=Json[-9:-5]
    
        with open(Json) as jsonFile:
            Objects=json.load(jsonFile)

        Image=cv2.imread(Image)
    
        imgH=Image.shape[0] #5000
        imgW=Image.shape[1] #5000

        if imgH!=5000 or imgW!=5000:
            cv2.resize(Image,dsize=(5000,5000),interpolation=cv2.INTER_AREA)
            imgH=5000
            imgW=5000

        mask=np.zeros((imgH,imgW,1))
        Compost_mask=np.zeros((imgH,imgW,1))
        C_mask=np.zeros((imgH,imgW,1))

        for idx in range(len(Objects['shapes'])):
            point=Objects['shapes'][idx]['points']
            point=np.array(point,np.int32)
            mask=cv2.fillConvexPoly(mask,point,255)    

            if Objects['shapes'][idx]['label']=="Compost":    
                Compost_mask=cv2.fillConvexPoly(Compost_mask,point,255)
            
            elif Objects['shapes'][idx]['label']=="Compost_C":
                C_mask=cv2.fillConvexPoly(C_mask,point,255)
        
        coordinate=np.where(mask==255)

        #해당이미지에 1%만 사용하기 위해 //100을 해줌
        PixelJump=len(coordinate[0])//100

        for n in range(self.n):
            mask_Dataset=np.zeros((224,224,2),dtype=np.uint8)
            Image_Dataset=np.zeros((224,224,3),dtype=np.uint8)

            try:
                x=coordinate[0][n*PixelJump]
                y=coordinate[1][n*PixelJump]
            except:
                pass

            mask_Dataset[:,:,0]=Compost_mask[x-PixelSize:x+PixelSize,y-PixelSize:y+PixelSize,0]
            mask_Dataset[:,:,1]=C_mask[x-PixelSize:x+PixelSize,y-PixelSize:y+PixelSize,0]

            Image_Dataset[:,:,:]=Image[x-PixelSize:x+PixelSize,y-PixelSize:y+PixelSize,:]
        
            np.save(self.route+"/Mask/mask_Dataset"+Name+"_"+str(n),mask_Dataset)
            np.save(self.route+"/Image/Image_Dataset"+Name+"_"+str(n),Image_Dataset)


route=os.getcwd()
compost_route=route+"/File"
JsonFile=glob(compost_route+"/*.json")
TifFile=glob(compost_route+"/*.tif")

CropSize=10000

m=MakeMask(route,JsonFile,TifFile,CropSize)
m.Makedir(route)
m.getFile()
