#!/usr/bin/python

import cv2
import numpy as np
from socketIO_client_nexus import SocketIO, LoggingNamespace
import RPi.GPIO as GPIO

ledErrorPin = 36
ledSuccessPin = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledErrorPin, GPIO.OUT)
GPIO.setup(ledSuccessPin, GPIO.OUT)

GPIO.output(ledErrorPin, GPIO.LOW)
GPIO.output(ledSuccessPin, GPIO.LOW)

socketIO = SocketIO("localhost", 2000, LoggingNamespace)

def decode(buf):
    nparr = np.fromstring(buf.decode("base64"), np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

def stream(buf):
    im = decode(buf)
    cv2.imshow("Stream", im)
    cv2.waitKey(1)

def unlock(nama):
    print("Diunlock oleh : {}".format(nama))
    GPIO.output(ledErrorPin, GPIO.LOW)
    GPIO.output(ledSuccessPin, GPIO.HIGH)

def neutral(args):
    print("Neutral")
    GPIO.output(ledErrorPin, GPIO.LOW)
    GPIO.output(ledSuccessPin, GPIO.LOW)

def invalid(data):
    print("Invalid")
    print(data)
    GPIO.output(ledErrorPin, GPIO.HIGH)
    GPIO.output(ledSuccessPin, GPIO.LOW)

# socketIO.on("stream", stream)

socketIO.on("unlock", unlock)
socketIO.on("neutral", neutral)
socketIO.on("invalid", invalid)

socketIO.wait()