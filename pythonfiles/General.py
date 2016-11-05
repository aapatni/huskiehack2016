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
    
<<<<<<< HEAD
faces = getFace(open("group-of-people-smiling-3794.jpg"), open("classifier.xml"))
image = open("group-of-people-smiling-3794.jpg")
=======
faces = getFace(open("group-of-people-smiling-3794.jpg"), )
print "Found {0} faces!".format(len(faces))

>>>>>>> 0bcdafb6de6f5db7b0d418b6b84cb55f5132c216
# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow("Faces found" ,image)
cv2.waitKey(0)