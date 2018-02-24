#!/usr/bin/python

import cv2
import numpy as np
from socketIO_client_nexus import SocketIO, LoggingNamespace

socketIO = SocketIO("localhost", 2000, LoggingNamespace)

def decode(buf):
    nparr = np.fromstring(buf.decode("base64"), np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

def stream(buf):
    im = decode(buf)
    cv2.imshow("Stream", im)
    cv2.waitKey(1)

socketIO.on("stream", stream)
socketIO.wait()