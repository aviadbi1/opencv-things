import os
import cv2
import numpy as np
import imutils


def resize_image(img, scale_percent):
    img = img.copy()
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return img


def crop_image(img, pts):
    # (1) Crop the bounding rect
    rect = cv2.boundingRect(pts)
    x, y, w, h = rect
    croped = img[y:y+h, x:x+w].copy()

    # (2) make mask
    pts = pts - pts.min(axis=0)

    mask = np.zeros(croped.shape[:2], np.uint8)
    cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)

    # (3) do bit-op
    dst = cv2.bitwise_and(croped, croped, mask=mask)

    # (4) add the white background
    bg = np.ones_like(croped, np.uint8)*255
    cv2.bitwise_not(bg, bg, mask=mask)
    dst2 = bg + dst
    return dst2


def save_image(img, name):
    cv2.imwrite(name, img)


def get_croped_images_from_scan(img, filename):
    img = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    ret, th = cv2.threshold(gray, 210, 235, 1)

    cnts, hierarchy = cv2.findContours(
        th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

    for index, c in enumerate(cnts):
        box = cv2.minAreaRect(c)
        box = cv2.boxPoints(box)
        box = np.array(box, dtype="int")
        box[box < 0] = 0
        Area = img.shape[0]*img.shape[1]
        if Area/10 < cv2.contourArea(box) < Area*2/3:
            # cv2.drawContours(img, [box], -1, (0, 255, 0), 2)
            # print(box)
            croped = crop_image(img, box)
            # cv2.imshow("croped", croped)
            save_image(croped, f'croped/{filename}_{index}.png')


directory = "photos"

for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        print(os.path.join(directory, filename))
        img = cv2.imread(os.path.join(directory, filename))

        # scale_percent = 20  # percent of original size
        # img = resize_image(img, scale_percent)
        try:
            get_croped_images_from_scan(img, filename)
        except cv2.error or TypeError as error:
            print(f'error: {error}')
    else:
        print(f'cannot read {filename}')


# cv2.imshow("Image", img)
# cv2.waitKey(0)
