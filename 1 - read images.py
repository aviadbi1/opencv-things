# Read images/videos/webcam

import cv2

img = cv2.imread("resources/me.jpg")
cv2.imshow('image', img)
cv2.waitKey(1)

# cap = cv2.VideoCapture('resources/vid.mp4')  # video is a sequence of images

cap = cv2.VideoCapture(0)  # webcam
cap.set(3, 640)  # width
cap.set(4, 480)  # heigth

while cap.isOpened():
    success, img = cap.read()
    cv2.imshow('video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # press Q for quit
