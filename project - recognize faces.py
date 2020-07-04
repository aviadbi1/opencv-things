import cv2
import numpy as np
import face_recognition
import os


def readFacesFromDir(dirPath):
    images = []
    classNames = []
    myList = os.listdir(dirPath)
    # print(myList)
    for faceClass in myList:
        curImg = cv2.imread(f'{dirPath}/{faceClass}')
        images.append(curImg)
        classNames.append(os.path.splitext(faceClass)[0])
    print(classNames)
    return images, classNames


def findEncodingsOfAFace(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def findFaceLocationInImage(img, imgName):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(img)
    for faceLoc in facesCurFrame:
        y1, x2, y2, x1 = faceLoc
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        # cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)

    cv2.imshow(imgName, img)


def identifyImage(img, imgName):
    scale = 2
    smallerImg = cv2.resize(img, (0, 0), None, 1.0/scale, 1.0/scale)
    smallerImg = cv2.cvtColor(smallerImg, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(smallerImg)
    encodesCurFrame = face_recognition.face_encodings(
        smallerImg, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDistance = face_recognition.face_distance(
            encodeListKnown, encodeFace)
        print(faceDistance)
        matchIndex = np.argmin(faceDistance)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            # print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*scale, x2*scale, y2*scale, x1*scale
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1+6, y2-6),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow(imgName, img)


dirPath = 'faces'
testDirPath = 'facesTest'

images, classNames = readFacesFromDir(dirPath)
encodeListKnown = findEncodingsOfAFace(images)
print('Encoding Complete')


testList = os.listdir(testDirPath)
for testFileName in testList:
    imgName = os.path.splitext(testFileName)[0]
    if testFileName.endswith("jpg"):
        curImg = cv2.imread(f'{testDirPath}/{testFileName}')
        identifyImage(curImg, imgName)
        # findFaceLocationInImage(curImg, imgName)

        cv2.waitKey(0)
    if testFileName.endswith('mp4'):
        cap = cv2.VideoCapture(f'{testDirPath}/{testFileName}')
        # cap = cv2.VideoCapture(0)  # videocam

        while cap.isOpened():
            success, img = cap.read()
            identifyImage(img, imgName)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break  # press Q for quit
