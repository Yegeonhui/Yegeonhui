import numpy as np

objp=np.zeros((9*7,3),np.float32)
objp[:,:2]=np.mgrid[0:9,0:7].T.reshape(-1,2)
print(objp)