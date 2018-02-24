#!/usr/bin/python

import collect
import cam

def start():
    print("Fast-face-door-unlocker")
    print("Pilih Menu")
    print("1. Perekaman")
    print("2. Kamera")
    print("3. Keluar")
    pilihan = int(raw_input("Masukkan pilihan : "))

    if(pilihan == 1):
        collect.start()
        start()
    elif(pilihan == 2):
        cam.start()
        start()
    elif(pilihan == 3):
        return
    else:
        print("Pilihan tidak valid")
        start()

start()