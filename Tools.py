from Tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np
import matplotlib.pyplot as plt
from ImageProcessing import ImageProcessing

# from tkFileDialog import askopenfilenames
from tkFileDialog import *

class Tools:
    root = None
    mainFrame = None
    btn = None
    canvas = None
    img = None
    positionOffset = 40
    imageLabel = None
    openedImage = None

    def __init__(self, root):
        print "In constructor"
        self.root = root
        self.imageLabel = Label(self.root, image=None)

    def openImage(self):
        imagePath = askopenfilenames(parent=self.root,filetypes=[("JPEG","*.jpg*"),("PNG","*.png*")])
        print imagePath

        if not imagePath:
            return
        self.openedImage = ImageProcessing(imagePath[0], self.root)
        self.updateImage(self.openedImage.getCvImg())

    def saveImage(self):
        filename = asksaveasfilename(parent=self.root,filetypes=[("PNG","*.png*"),("JPEG","*.jpg*")],initialfile= self.openedImage.getImageNameWithExtension(),defaultextension="*.*")
        print "Path to save"
        print filename
        if filename:
            cv2.imwrite(filename, self.openedImage.getCvImg())
        pass

    def updateImage(self, cvImg):
        cvImg = cv2.cvtColor(cvImg, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(cvImg)
        tkImage = ImageTk.PhotoImage(image=im)

        self.imageLabel.configure(image=tkImage)
        self.imageLabel.image = tkImage
        self.imageLabel.pack()

    def adjustWindowSizeToImage(self):
        pass
