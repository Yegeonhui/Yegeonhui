import numpy as np
import cv2
from glob import glob
import os

route=os.getcwd()
Mask_List=glob(route+"/Mask/*.npy")
Image_List=glob(route+"/Image/*.npy")

print(Mask_List)
for file in range(len(Mask_List)): 

    Mask=np.load(Mask_List[file])
    Image=np.load(Image_List[file])
    
    mask_Compost=Mask[:,:,0]
    mask_Compost_C=Mask[:,:,1]

    cv2.imshow("image",Image)
    cv2.imshow("mask",mask_Compost)
    cv2.imshow("mask!",mask_Compost_C)
    cv2.waitKey(0)
    cv2.destroyAllWindows()                                    