import numpy as np
import cv2
# Load an color image in grayscale
img = cv2.imread('flori.png',1)
cv2.imshow('flori.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
img = cv2.imread('flori.png',0)
cv2.imshow('flori.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()