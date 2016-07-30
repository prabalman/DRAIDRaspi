import pickle
import socket
import struct
import sys

import numpy as np

import cv2

HOST = '127.0.0.1'
PORT = 8082

cap = cv2.VideoCapture(0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST, PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')

conn, addr = s.accept()

while True:
    ret, frame = cap.read()
    data = pickle.dumps(frame)
    conn.sendall(struct.pack("L", len(data)) + data)
