
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


import cv2

img=cv2.imread("Shapes.png")
dimension=(100,100)
resized=cv2.resize(img,dimension)

cv2.imshow('output',resized)
cv2.waitKey()


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
"""
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

t1 = threading.Thread(target=printsquare, args=(10,))
t2 = threading.Thread(target=printcube, args=(10,))
#printsquare(10)
t1.start()
t2.start()
#t1.join()
#t2.join()
print("Done!")
