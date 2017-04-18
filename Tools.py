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

    def addEyeFilter(self):
        print "Inside adding eye filter"
        self.openedImage.detectFaces()
        self.fList = self.openedImage.getDetectedFaces()

        imgHeight, imgWidth = self.openedImage.getCvImgDimensions()
        print "Height:" + str(imgHeight) + " Width:" + str(imgWidth)
        cvImg = cv2.cvtColor(self.openedImage.getCvImg(), cv2.COLOR_BGR2RGB)
        im = Image.fromarray(cvImg)
        self.canvas = Canvas(self.root, height=imgHeight, width=imgWidth)
        self.canvas.grid()

        self.backgnd = ImageTk.PhotoImage(image=im)

        self.filterImage = ImageTk.PhotoImage(file="Images/Filters/Eyes/eye.png")
        backgnd_width = (self.backgnd.width() / 2)
        backgnd_height = (self.backgnd.height() / 2)
        self.canvas.create_image(backgnd_width, backgnd_height, image=self.backgnd)

        print "Entering for loop"
        for face in self.fList:
            print "x:" + str(face['fx']) + " y:" + str(face['fy']) + " w:" + str(face['fw']) + " h:" + str(face['fh'])
            for eye in face['eyes']:
                print "ex:" + str(eye['ex']) + " ey:" + str(eye['ey']) + " ew:" + str(eye['ew']) + " eh:" + str(eye['eh'])
                avgX = ((face['fx'] + eye['ex']) + (face['fx'] + eye['ex'] + eye['ew']))/2
                avgY = ((face['fy'] + eye['ey']) + (face['fy'] + eye['ey'] + eye['eh'])) / 2
                self.canvas.create_image(avgX, avgY, image=self.filterImage)

        pass
