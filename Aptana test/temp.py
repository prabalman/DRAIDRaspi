import cv2
import numpy as np


"""load the cascade given for facial detection and eye detection
    CascadeClassifier functions takes path
 """
face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_eye.xml')

#read image from relative directory
img = cv2.imread('test.jpg')

#convert the image into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

""" 
    Detect images via detectMultiScale function(imgsrc,scaleFactor,
    minNeighbours,minSIze,flags)
    Returns list of rectangles where a face is found
"""
faces = face_cascade.detectMultiScale(gray, 1.3, 3)

for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #Draw rectangle around faces
    roi_gray = gray[y:y+h, x:x+w]#ROI where there are faces
    roi_color = img[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(roi_gray)#Same
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()