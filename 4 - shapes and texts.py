# Shaped and Texts

import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# print(img.shape)  # 3 so BGR
# img[200:300, 100:300] = 255, 0, 0  # blue

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (100, 200, 100), 3)
cv2.rectangle(img, (100, 100), (200, 400), (0, 0, 255), 3)
cv2.circle(img, (100, 100), 40, (255, 0, 255), cv2.FILLED)
cv2.putText(img, "Hi there", (300, 100),
            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)


cv2.imshow("img", img)

cv2.waitKey(0)
