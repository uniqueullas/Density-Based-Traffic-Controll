"""
import cv2
img=cv2.imread("Shapes.png")

scale_percentage = 0.50
width=int(img.shape[1]*scale_percentage)
height=int(img.shape[0]*scale_percentage)
dimesion=(width,height)

resized=cv2.resize(img,dimesion,interpolation=)
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("image")

my_img = Image.open("Shapes.png")
resized = my_img.resize((100, 100),Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)
mylabel = Label(image=new_pic, height=100, width=100)
mylabel.pack(pady=20)


button_quit = Button(root,text="exit",command=root.quit)
button_quit.pack()
root.mainloop()







