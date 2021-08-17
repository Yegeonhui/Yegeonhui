from PIL import Image
from PIL.ExifTags import TAGS
import os
import cv2
import json
import math
#매트릭스,왜곡계수,회전/변환벡터

route=os.getcwd()
route_red=route+"/correction.jpg"

img=cv2.imread(route_red)
height,width=img.shape[:2]
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#사각형 한변구하기(pixel)
with open("correction.json") as jsonFile:
    Objects=json.load(jsonFile)
    point=Objects['shapes'][0]['points']
print(point)

result=[0]*4
for i in range(3,-1,-1):
    result[i]=math.sqrt(abs(point[i][0]-point[i-1][0])**2+abs(point[i][1]-point[i-1][1])**2)
print(result)

pixel_r=(result[0]+result[2])/2
pixel_c=(result[1]+result[3])/2
print(pixel_r,pixel_c)
print(height,width)

# route_red=route+"/red.jpg"
# img=Image.open(route_red)
# info=img._getexif()
# taglabel={}
# for tag,value in info.items():
#     decoded=TAGS.get(tag)
#     taglabel[decoded]=value
