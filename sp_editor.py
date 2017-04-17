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
    tools = None

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


        pass

    def openImage(self):
        self.tools.openImage()

    def saveImage(self):
        self.tools.saveImage()
        pass


    def quit(self):
        print("Closing Program...")
        self.destroy()


startSpEditor = SpEditor()
startSpEditor.mainloop()
