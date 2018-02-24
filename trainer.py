#!/usr/bin/python

import cv2, os
import numpy as np
from PIL import Image

if(cv2.__version__ == '3.2.0'):
    recognizer = cv2.face.createLBPHFaceRecognizer()
else:
    recognizer = cv2.face.LBPHFaceRecognizer_create()

detector = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')

def getImageAndLabels(path):

    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

    faceSamples = []

    ids = []

    for imagePath in imagePaths:

        PIL_img = Image.open(imagePath).convert('L')

        img_numpy = np.array(PIL_img, 'uint8')

        id = int(os.path.split(imagePath)[-1].split('.')[1])

        print(id)

        faces = detector.detectMultiScale(img_numpy)

        for (x, y, w, h) in faces:

            faceSamples.append(img_numpy[y:y+h, x:x+w])

            ids.append(id)

        
    return faceSamples, ids


faces, ids = getImageAndLabels('./datasets')

recognizer.train(faces, np.array(ids))

if(cv2.__version__ == '3.2.0'):
    recognizer.save('./training/trainer.yml')
else:
    recognizer.write('./training/trainer.yml')