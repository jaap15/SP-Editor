from Tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np
import matplotlib.pyplot as plt
from ImageProcessing import ImageProcessing

from tkFileDialog import askopenfilenames

class Tools:
    root = None
    mainFrame = None
    btn = None
    canvas = None
    img = None
    positionOffset = 40
    imageLabel = None

    def __init__(self, root):
        print "In constructor"
        self.root = root
        self.imageLabel = Label(self.root)

    def openImage(self):
        self.imagePath = askopenfilenames(parent=self.root,filetypes=[("JPEG","*.jpg*"),("PNG","*.png*")])
        print self.imagePath

        if not self.imagePath:
            return

        cvimg = cv2.imread(self.imagePath[0], cv2.IMREAD_GRAYSCALE)
        im = Image.fromarray(cvimg)
        self.img = ImageTk.PhotoImage(image=im)
        self.imageLabel = Label(self.root, image=self.img)
        self.imageLabel.pack()
        openedImage = ImageProcessing()
        # self.updateImage(openedImage.getTkImage())


    def updateImage(self, tkImage):
        self.imageLabel.configure(image=tkImage)
        self.imageLabel.image = tkImage

    def getImagePath(self):
        return self.imagePath

    def adjustWindowSizeToImage(self):
        pass