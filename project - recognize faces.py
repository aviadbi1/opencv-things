import cv2
import face_recognition

imgLior = face_recognition.load_image_file('faces/Lior.jpg')
imgLior = cv2.cvtColor(imgLior, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('faces/JamesCorden.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgLior)[0]
encodeLior = face_recognition.face_encodings(imgLior)[0]
cv2.rectangle(imgLior, (faceLoc[3], faceLoc[0]),
              (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]),
              (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

results = face_recognition.compare_faces([encodeLior], encodeTest)
faceDis = face_recognition.face_distance([encodeLior], encodeTest)
print(results, faceDis)
cv2.putText(imgTest, f'{results} {round(faceDis[0],2)}', (
    50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('Lior Suchard', imgLior)
cv2.imshow('Lior?', imgTest)
cv2.waitKey(0)
