# WARP Prespective

import cv2
import numpy as np

img = cv2.imread("resources/cards.jpg")

width, height = 250, 350
pts1 = np.float32([[180, 40], [260, 105], [15, 125], [90, 190]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("cards", img)
cv2.imshow("cards output", imgOutput)

cv2.waitKey(0)
