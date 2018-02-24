#!/usr/bin/python

import mysql.connector

cnx = mysql.connector.connect(user="root",password="sirius221b#$;",host="127.0.0.1",database="face_rec")

def simpan(nama):
    cursor = cnx.cursor()
    query = ("INSERT INTO ids (nama) VALUES ('{}')".format(nama))
    cursor.execute(query)
    id = cursor.lastrowid
    cnx.commit()
    cursor.close()
    return id

def getNama(id):
    cursor = cnx.cursor()
    query = ("SELECT * FROM ids WHERE id = {}".format(id))
    cursor.execute(query)
    dapat = False
    for (id, nama) in cursor:
        if(nama is not None):
            dapat = nama
            break
    cursor.close()
    return dapat