#!/usr/bin/python
import cv2
import numpy as np
import base64

if(cv2.__version__ == '3.2.0'):
    recognizer = cv2.face.createLBPHFaceRecognizer()
else:
    recognizer = cv2.face.LBPHFaceRecognizer_create()

if(cv2.__version__ == '3.2.0'):
    recognizer.load('./training/trainer.yml')
else:
    recognizer.read('./training/trainer.yml')

cascadePath = './cascades/haarcascade_frontalface_default.xml'

faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

cam = cv2.VideoCapture(0)

padding = 20

while True:

    name = 'Tidak dikenal'

    ret, im = cam.read()

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.5, 5)

    for (x, y, w, h) in faces:
        
        cv2.rectangle(im, (x-padding, y-padding), (x+w+padding, y+h+padding), (0, 255, 0), 2)

        id, level_cocok = recognizer.predict(gray[y:y+h, x:x+w])
        print(id)
        print(level_cocok)

        if(level_cocok < 70):
            if(id == 1):
                name = 'Edgar'
            elif(id == 2):
                name = "Melqu"
        else:
            name = 'Tidak dikenal'

        cv2.rectangle(im, (x-22, y-90), (x+w+22, y-22), (0, 255, 0), -1)
        cv2.putText(im, str(name), (x, y-40), font, 2, (255,255,255), 3)

    cv2.imshow('Feed', im)
    
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cam.release()
cv2.destroyAllWindows()
