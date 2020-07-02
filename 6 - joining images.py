# Joining images

import cv2
import numpy as np

img = cv2.imread("resources/cards.jpg")

imgHoirzontal = np.hstack((img,img))
imgVertical = np.vstack((img,img))

cv2.imshow("imgHoirzontal", imgHoirzontal)
cv2.imshow("imgVertical", imgVertical)

cv2.waitKey(0)
