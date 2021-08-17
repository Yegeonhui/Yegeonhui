import numpy as np
import os
import cv2
import json


class MakeDataset:
    def __init__(self, JsonName):
        self.JsonName = JsonName

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
     
        elif len(Objects['shapes']) > 1:
            mask = np.zeros((imgH, imgW, 1))
            for idx in range(len(Objects['shapes'])):
                point = Objects['shapes'][idx]['points']
                point = np.array(point, np.int32)
                mask = cv2.fillConvexPoly(mask, point, 255) 

        return mask
    
    def saveMask(self):
        mask = self.getMask()

        maskName = self.JsonName[:-5] + '.jpg'

        cv2.imwrite(maskName, mask)

mask=MakeDataset("1.json")
mask.saveMask()


