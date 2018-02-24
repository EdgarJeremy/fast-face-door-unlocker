#!/usr/bin/python

import cv2
import db
import trainer

def start():

    vid_cam = cv2.VideoCapture(0)
    face_detector = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')

    nama = raw_input("Masukkan Nama : ")
    print("Menginput ke database...")
    face_id = db.simpan(nama)
    print("Tersimpan {} dengan id {}".format(nama,face_id))
    count = 0
    samples = 100
    start = False

    print("Perekaman siap, letakkan wajah di dalam kotak hijau dan tekan tombol `s` jika sudah siap")

    while(True):

        _, image_frame = vid_cam.read()

        gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        imw, imh, imc = image_frame.shape

        cv2.rectangle(image_frame, (200, 100), (imh - 200, imw - 100), (0,255,0), 2)

        if cv2.waitKey(1) & 0xFF == ord('s') or start:
            for (x, y, w, h) in faces:

                cv2.rectangle(image_frame, (x,y), (x+w, y+h), (255, 0, 0))

                count += 1

                cv2.imwrite('./datasets/User.' + str(face_id) + '.' + str(count) + '.jpg', gray[y:y+h, x:x+w])

                start = True

            print("Mengambil wajah ({}%)".format(count))

        
        cv2.imshow('Rekam', image_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif count >= samples:
            break

    vid_cam.release()
    cv2.destroyAllWindows()

    print("Perekaman berhasil")

    trainer.start()