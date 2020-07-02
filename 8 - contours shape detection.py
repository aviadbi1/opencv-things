# Contours / Shape Detection

import cv2
import numpy as np

path = "resources/shapes.png"
img = cv2.imread(path)
imgContour = img.copy()


def getContours(img):
    contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            # draw the contour on the image
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            arcLength = cv2.arcLength(cnt, True)

            # 3 triangle 4 square more is circle
            approx = cv2.approxPolyDP(cnt, 0.03*arcLength, True)
            print("approximate polygonal curves", len(approx))
            x, y, width, height = cv2.boundingRect(approx)
            objectType = "Circle"
            if len(approx) == 3:
                objectType = "Triangle"
            elif len(approx) == 4:
                objectType = "Rectangle"

            # draw rect and text on the image
            cv2.rectangle(imgContour, (x, y),
                          (x+width, y+height), (100, 100, 100), 2)
            cv2.putText(imgContour, objectType, (x+(width//2) - 20, y+(height//2)),
                        cv2.FONT_HERSHEY_PLAIN, 0.8, (255, 255, 255), 1)


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)


#cv2.imshow("original", img)
#cv2.imshow("gray", imgGray)
#cv2.imshow("blur", imgBlur)
cv2.imshow("imgCanny", imgCanny)
cv2.imshow("imgContour", imgContour)
cv2.waitKey(0)
