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
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags = cv2.cv.CV_HAAR_SCALE_IMAGE)
    area = [0, 0]
    for i in faces:
        if i[2]*i[3] > area[1]:
            area[1] = i[2]*i[3]
            area[0] = i
    return area[0]
def getEyes(imgPath, cPath, face):
    image = cv2.imread(imgPath)
    # Create the haar cascade
    eyeCascade = cv2.CascadeClassifier('eyeclassifier.xml')
    # Read the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    roi = gray[face[1]:face[1]+face[3], face[0]:face[0]+face[2]]
    # Detect faces in the image
    teyes = eyeCascade.detectMultiScale(roi)
    #teyes = teyes[0:2]
    return teyes
def getNose(imgPath, cPath, face):
    image = cv2.imread(imgPath)
    
    # Create the haar cascade
    noseCascade = cv2.CascadeClassifier(cPath)
    # Read the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    roi = gray[face[1]:face[1]+face[3], face[0]:face[0]+face[2]]
    # Detect faces in the image
    tnose = noseCascade.detectMultiScale(roi)
    return tnose
    
def findCenter(array):
    centers = []
    for i in array:
        x = int(i[0] + (.5)*(i[2]))
        y = int(i[1] + (.5)*(i[3]))
        centers.append([x,y])
    return centers
#finds the center between eyes. this is the bridge of nose position

def findBridge(center_eyes):
    bridge_x = center_eyes
faces = getFace("./picture.jpg", "./faceclassifier.xml")
eyes = getEyes("./picture.jpg", "./eyeclassifier.xml", faces)
nose = getNose("./picture.jpg", "./noseclassifier.xml", faces)
image = open("./picture.jpg")
center_eyes = findCenter(eyes)
facex = faces[0]
facey = faces[1]
facew = faces[2]
faceh = faces[3]

#for (x, y, w, h) in faces:
#    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
#cv2.imshow("Faces found" ,image)
#cv2.waitKey(0)
print "Faces:\n%s\nEyes:\n%s\nFaces:\n%s\nEyes:\n%s\n"
