from Tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

class ImageProcessing:

    tkImage = None
    imageFullPath = None
    imageName = None
    extension = None
    root = None
    cvimg = None
    faceCascade = None
    eyeCascade = None
    facesList = []

    def __init__(self, imageFullPath, root):
        print "In constructor"
        self.imageFullPath = imageFullPath
        self.root = root

        self.imageName, self.extension = os.path.splitext(imageFullPath)
        self.cvimg = cv2.imread(self.imageFullPath)

        self.faceCascade = cv2.CascadeClassifier('HaarCascades/haarcascade_frontalface_default.xml')
        self.eyeCascade = cv2.CascadeClassifier('HaarCascades/haarcascade_eye.xml')

    def detectFaces(self):
        gray = cv2.cvtColor(self.cvimg, cv2.COLOR_BGR2GRAY)
        faces = self.faceCascade.detectMultiScale(gray, 1.3, 5)
        i = 1
        j = 1
        for (x,y,w,h) in faces:
            print "Face " + str(i)
            print "x:" + str(x) + " y:" + str(y) + " w:" + str(w) + " h:" + str(h)
            roi_gray = gray[y:y+h, x:x+w]
            eyes = self.eyeCascade.detectMultiScale(roi_gray)
            eyeList = []
            for (ex,ey,ew,eh) in eyes:
                print "Eye " + str(j)
                print "ex:" + str(ex) + " ey:" + str(ey) + " ew:" + str(ew) + " eh:" + str(eh)
                eyeList.append({'ex':ex,'ey':ey,'ew':ew,'eh':eh})
                j = j + 1
            self.facesList.append({'fx':x,'fy':y,'fw':w,'fh':h,'eyes': eyeList})
            i = i + 1
        pass

    def getDetectedFaces(self):
        return self.facesList

    def getCvImgDimensions(self):
        return self.cvimg.shape[:2]

    def getTkImage(self):
        im = Image.fromarray(self.cvimg)
        self.tkImage = ImageTk.PhotoImage(image=im)
        return self.tkImage

    def getCvImg(self):
        return self.cvimg

    def setTkImage(self, tkImage):
        self.tkImage = tkImage

    def getImageFullPath(self):
        return self.imageFullPath

    def setImageFullPath(self, imageFullPath):
        self.imageFullPath = imageFullPath

    def getImageNameWithExtension(self):
        return self.imageName + self.extension