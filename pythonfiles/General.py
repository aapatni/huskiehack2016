#!/usr/bin/python

import cv2
import os,sys

def getFace(imgPath, cPath):

    image = cv2.imread(imgPath)
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cPath)
    # Read the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image
    return faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags = cv2.cv.CV_HAAR_SCALE_IMAGE)
    
faces = getFace("./picture.jpg", "./classifier.xml")
image = open("./picture.jpg")
#for (x, y, w, h) in faces:
#    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
#cv2.imshow("Faces found" ,image)
#cv2.waitKey(0)
print faces

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
         cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = img[y:y+h, x:x+w]
         eyes = eye_cascade.detectMultiScale(roi_gray)
         for (ex,ey,ew,eh) in eyes:
    8         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    9 
   10 cv2.imshow('img',img)
   11 cv2.waitKey(0)
   12 cv2.destroyAllWindows()
