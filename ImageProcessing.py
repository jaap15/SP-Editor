from Tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np
import matplotlib.pyplot as plt

class ImageProcessing:

    tkImage = None
    imageFullPath = None
    imageName = None

    def __init__(self):
        print "In constructor"

    def getTkImage(self):
        cvimg = cv2.imread("watch.jpg", cv2.IMREAD_GRAYSCALE)
        im = Image.fromarray(cvimg)
        self.tkImage = ImageTk.PhotoImage(image=im)
        return self.tkImage