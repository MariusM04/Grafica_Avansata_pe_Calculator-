import cv2
img = cv2.imread('flori.png')
# conversie imagine grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Initiaza FAST object with default values
fast = cv2.FastFeatureDetector_create()
# Gaseste keypoints pe imagagine (grayscale)
kp = fast.detect(gray,None)
# Deseneaza keypoints in imagagine
img2 = cv2.drawKeypoints(img, kp, None)
# Print toti parametrii
print("Threshold: ", fast.getThreshold())
print("nonmaxSuppression: ", fast.getNonmaxSuppression())
print("neighborhood: ", fast.getType())
print("Total Keypoints with nonmaxSuppression: ", len(kp))
# Imagagine cu keypoints desenate pe aceasta
cv2.imshow("Keypoints with nonmaxSuppression", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()