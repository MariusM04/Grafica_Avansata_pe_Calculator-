import cv2
import numpy as np

poza = ('flori.png')
imagine = cv2.imread(poza)

gray = cv2.cvtColor(imagine,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.05)

dst = cv2.dilate(dst,None)

imagine[dst>0.01*dst.max()]=[0,0,255]
cv2.imshow('dst', imagine)
if cv2.waitKey(0) & 0xff == 25:
    cv2.destroyAllWindows()