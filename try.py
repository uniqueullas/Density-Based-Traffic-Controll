
"""
import cv2
img=cv2.imread("Shapes.png")

scale_percentage = 0.50
width=int(img.shape[1]*scale_percentage)
height=int(img.shape[0]*scale_percentage)
dimesion=(width,height)

resized=cv2.resize(img,dimesion,interpolation=)


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

def hu():
    print("i am hu")

def numbers_to_strings(argument):
    switchr = {
        'Manual Mode': hu(),
        1: "one",
        2: "two",
    }

    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    #return switcher.get(argument, "nothing")
    return switchr.get(argument,'hu()')


# Driver program
#if __name__ == "__main__":
argument = 'Manual Mode'
print (numbers_to_strings(argument))


import time

milli_delay = (int(round(time.time()+5)))
pmili = (int(round(time.time())))
while(milli_delay > pmili):
    time.sleep(1)
    pmili = (int(round(time.time())))
    print(milli_delay - pmili)
print("finished..!")


a = [1,2,5,3]
print(type(a[2]))

# Python program to illustrate the concept
# of threading
# importing the threading module
import threading
import time
flag = False

def printcube(num):
    print("Cube")
    while (flag == False):
        print("waiting")
    print("Cube: {}".format(num * num * num))

def printsquare(num):
    global flag
    time.sleep(1)
    flag = True
    print("Square: {}".format(num * num))


t1 = threading.Thread(target=printsquare, args=(10, ))
t2 = threading.Thread(target=printcube, args=(10, ))
#printsquare(10)
t1.start()
t2.start()
#t1.join()
#t2.join()
print("Done!")

import time
def t():
    print("eeeeeeeeeeee")
    time.sleep(3)

def pr():
    t()
    print("uuuuuuuuuuuuuuuuu")
    time.sleep(2)

print("-----------------")
pr()
print("++++++++++++++++++")


from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):
    def build(self):
        return Button(text='Hello World')
    def build(self):
        return Button(text='Hello')

TestApp().run()



from tkinter import *
import tkinter.font as tkFont
import time
import threading

def User_input_GUI():
    CURRENT_TRAFFIC_MODE = "Normal Mode"

    root = Tk()
    root.geometry("601x700")
    root.title("Telaverge Communications")
    root.iconbitmap("TELALOGO.ico")
    title = tkFont.Font(family="impact", size = 30)
    heading_1 = tkFont.Font(family="Lucida Grande", size=10, )

    Label(root, text="Density", fg = 'black', font=title).grid(row=0, column=0)
    Label(root, text=" Based Smart", fg='black', font=title).grid(row=0, column=1)
    Label(root, text=" Traffic", fg='black', font=title).grid(row=0, column=2)
    Label(root, text=" Control", fg='black', font=title).grid(row=0, column=3)
    print("--------------------------------------------------------------------------------------")

    def again():
        i = ti()
        ser = str(i)
        Label(root, text=ser, fg='black', font=heading_1).grid(row=2, column=2)
        root.after(1000, again)

    def ti():
        i_a = (int(round(time.time())))
        return i_a

    again()
    root.mainloop()


#for i in range(5):
        #print(i)
        #ser = str(i)

User_input_GUI()
#for i in range(2, 5):
#print(i)


import cv2

dimension=(120,130)
sidea=cv2.resize(cv2.imread("Shapes.png"),dimension)
cv2.imshow('output', sidea)
cv2.imwrite("Shapes_resized.png", sidea)
cv2.waitKey()
"""
from tkinter import *

top = Tk()
sb = Scrollbar(top)
sb.grid(row=0, column=5, columnspan=2, rowspan=20, sticky=E+S)
#sb.pack(side=RIGHT, fill=Y)

mylist = Listbox(top, yscrollcommand=sb.set)

for line in range(30):
    mylist.insert(END, "Number " + str(line))

mylist.grid(row=0,column=0)
sb.config(command=mylist.yview)

mainloop()