# Resizing and cropping

import cv2

img = cv2.imread("resources/me.jpg")
print(img.shape)  # (height, width, channels 'BGR')

imgResize = cv2.resize(img, (230, 300))
print(imgResize.shape)  # (height, width, 'BGR')

imgCropped = img[100:200, 300:600]

cv2.imshow("img", img)
cv2.imshow("imgResize", imgResize)
cv2.imshow("imgCropped", imgCropped)

cv2.waitKey(0)
