import numpy as np
import cv2
import sys
import argparse
from thre import WebcamStream

def video_face():
    face = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
    eye = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_eye.xml')
    
#vid = cv2.VideoCapture(0)
    vid = WebcamStream(src=0)
    vid.start()
    while(1):
        frame = vid.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face1 = face.detectMultiScale(gray,1.3,5)
        
        for(x,y,w,h) in face1:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+h]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
        resz = cv2.resize(frame,(1920,1080))
        vid.rea().write(frame)
        sys.stdout.write(frame.tostring())
        cv2.imshow('img',resz)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

       
        
        

    cv2.destroyAllWindows()
    vid.stop()

if __name__ == "__main__":
    video_face()
    