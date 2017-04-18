from Tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np
import matplotlib.pyplot as plt
from ImageProcessing import ImageProcessing

# from tkFileDialog import askopenfilenames
from tkFileDialog import *
import io

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
        # self.canvas.
        self.canvas = None
        self.openedImage = None
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
        if cv2 == "":
            self.imageLabel.configure(image="")
            # self.imageLabel.image = tkImage
            self.imageLabel.pack()
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
        self.imageLabel.pack_forget()
        self.openedImage.clearFaces()
        self.openedImage.detectFaces()
        self.fList = self.openedImage.getDetectedFaces()

        imgHeight, imgWidth = self.openedImage.getCvImgDimensions()
        print "Height:" + str(imgHeight) + " Width:" + str(imgWidth)
        cvImg = cv2.cvtColor(self.openedImage.getCvImg(), cv2.COLOR_BGR2RGB)
        im = Image.fromarray(cvImg)

        self.canvas = Canvas(self.root, height=imgHeight, width=imgWidth)
        self.canvas.grid()

        self.backgnd = ImageTk.PhotoImage(image=im)

        self.appliedFilters = []

        backgnd_width = (self.backgnd.width() / 2)
        backgnd_height = (self.backgnd.height() / 2)
        self.canvas.create_image(backgnd_width, backgnd_height, image=self.backgnd)

        print "Entering for loop"
        i = 0
        for face in self.fList:
            print "x:" + str(face['fx']) + " y:" + str(face['fy']) + " w:" + str(face['fw']) + " h:" + str(face['fh'])
            for eye in face['eyes']:
                print "ex:" + str(eye['ex']) + " ey:" + str(eye['ey']) + " ew:" + str(eye['ew']) + " eh:" + str(eye['eh'])
                avgX = ((face['fx'] + eye['ex']) + (face['fx'] + eye['ex'] + eye['ew']))/2
                avgY = ((face['fy'] + eye['ey']) + (face['fy'] + eye['ey'] + eye['eh'])) / 2
                image = Image.open("Images/Filters/Eyes/eye1.png")
                image.thumbnail((eye['ew'],eye['eh']), Image.ANTIALIAS)
                self.appliedFilters.append(ImageTk.PhotoImage(image=image))
                self.canvas.create_image(avgX, avgY, image=self.appliedFilters[i])
                i = i + 1
        pass

    def removeFilter(self):
        del self.appliedFilters[:]
        self.backgnd = None
        del self.backgnd
        self.canvas.destroy()
        self.canvas = None
        self.updateImage(self.openedImage.getCvImg())
