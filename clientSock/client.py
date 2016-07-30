import pickle
import socket
import struct
import sys

import numpy as np

import cv2

HOST = '127.0.0.1'
PORT = 8082


clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((HOST, PORT))


data = bytes()
payload_size = struct.calcsize("L")

while True:
    while len(data) < payload_size:
        data += clientsocket.recv(4096)
    packed_msg_size = data[:payload_size]

    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]

    while len(data) < msg_size:
        data += clientsocket.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]

    frame = pickle.loads(frame_data)
    print(frame.size)
    cv2.imshow('SERVER', frame)
    cv2.waitKey(10)
