from Tkinter import *


def openImage():
    print("Opening image...")


def quit(root):
    print("Closing Program...")
    root.destroy()

root = Tk()
root.title("SP-Editor")
menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu)
menu.add_cascade(label= "File", menu=fileMenu)

fileMenu.add_command(label= "Open", command=openImage)

fileMenu.add_separator()
fileMenu.add_command(label= "Exit", command=lambda root=root:quit(root))

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)

root.mainloop()