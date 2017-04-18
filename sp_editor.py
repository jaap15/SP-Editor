from Tkinter import *
import Tkinter as tk
from PIL import Image, ImageTk
import cv2
import numpy as np
import matplotlib.pyplot as plt

from ImageProcessing import ImageProcessing
from Tools import Tools


class SpEditor(tk.Tk):
    menu = None
    fileMenu = None
    editMenu = None
    filterMenu = None
    tools = None
    canvas = None
    photo = None

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.tools = Tools(self)
        self.title("SP-Editor")
        self.menu = Menu(self)
        self.config(menu=self.menu)
        self.fileMenu = tk.Menu(self.menu)
        self.menu.add_cascade(label= "File", menu=self.fileMenu)

        self.fileMenu.add_command(label= "Open", command=self.openImage)

        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Save As", command=self.saveImage)

        self.fileMenu.add_separator()
        self.fileMenu.add_command(label= "Exit", command=self.quit)

        self.editMenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Edit", menu=self.editMenu)

        self.filterMenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Filters", menu=self.filterMenu)

        self.filterMenu.add_command(label="Stressed Eyes", command=self.bigEyeFilter)

        self.filterMenu.add_command(label="In Love", command=self.inLoveFilter)

        self.filterMenu.add_command(label="Cartoon Eye", command=self.cartoonEyeFilter)

        self.filterMenu.add_command(label="Remove Filter", command=self.rmFilter)


    def openImage(self):
        self.tools.openImage()

    def saveImage(self):
        self.tools.saveImage()
        pass

    def bigEyeFilter(self):
        self.tools.addEyeFilter("stressedEye")

    def inLoveFilter(self):
        self.tools.addEyeFilter("inLove")

    def cartoonEyeFilter(self):
        self.tools.addEyeFilter("cartoonEye")

    def rmFilter(self):
        self.tools.removeFilter()

    def quit(self):
        print("Closing Program...")
        self.destroy()


startSpEditor = SpEditor()
startSpEditor.mainloop()
