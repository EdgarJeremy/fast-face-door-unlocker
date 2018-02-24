#!/usr/bin/python

import cv2

vid_cam = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')

face_id = raw_input("Masukkan ID : ")
count = 0
samples = 300

while(True):

    _, image_frame = vid_cam.read()

    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:

        cv2.rectangle(image_frame, (x,y), (x+w, y+h), (255, 0, 0))

        count += 1

        cv2.imwrite('./datasets/User.' + str(face_id) + '.' + str(count) + '.jpg', gray[y:y+h, x:x+w])

    print(count)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif count > samples:
        break

vid_cam.release()
cv2.destroyAllWindows()