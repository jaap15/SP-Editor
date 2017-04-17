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

    def __init__(self, imageFullPath, root):
        print "In constructor"
        self.imageFullPath = imageFullPath
        self.root = root

        self.imageName, self.extension = os.path.splitext(imageFullPath)
        self.cvimg = cv2.imread(self.imageFullPath)

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