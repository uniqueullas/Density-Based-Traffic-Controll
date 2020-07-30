from tkinter import *
import tkinter.font as tkFont
CURRENT_TRAFFIC_MODE = "Normal Mode"

def gui(CURRENT_TRAFFIC_MODE):
    CURRENT_TRAFFIC_MODE = CURRENT_TRAFFIC_MODE
    root = Tk()
    root.geometry("700x500")
    root.title("Telaverge Communications")
    title = tkFont.Font(family="impact", size=30)
    heading_1 = tkFont.Font(family="Lucida Grande", size=10,)
    heading_2 = tkFont.Font(family="Lucida Grande", size=10)

    myLabel1 = Label(root, text="Density Based",fg='black',font= title)
    myLabel1.grid(row=0, column=0)
    myLabel1f = Label(root, text=" Smart Traffic ", fg='black', font=title)
    myLabel1f.grid(row=0, column=1)
    myLabel1l = Label(root, text=" Control", fg='black', font=title)
    myLabel1l.grid(row=0, column=2)


    myLabel2 = Label(root, text="MINIMUM_VEHICLE", fg='black', font=heading_1)
    myLabel2.grid(row=1, column=0)
    #myLabel2.pack()
    MINIMUM_VEHICLE= Entry(root,font=heading_1) #ney
    #MINIMUM_VEHICLE.pack()
    MINIMUM_VEHICLE.grid(row=1, column=1)

    myLabel3 = Label(root, text="TRAFFIC_TIME", fg='black', font=heading_1)
    #myLabel3.pack()
    myLabel3.grid(row=2, column=0)
    TRAFFIC_TIME= Entry(root, font=heading_1) #eey
    #TRAFFIC_TIME.pack()
    TRAFFIC_TIME.grid(row=2, column=1)

    myLabel4 = Label(root, text="VEHICLE_PASS_TIME", fg='black', font=heading_1)
    #myLabel4.pack()
    myLabel4.grid(row=3, column=0)

    VEHICLE_PASS_TIME=Entry(root, font=heading_1) #eey
    #VEHICLE_PASS_TIME.pack()
    VEHICLE_PASS_TIME.grid(row=3, column=1)


    def submit():
        print("MINIMUM_VEHICLE :",MINIMUM_VEHICLE.get())
        print("TRAFFIC_TIME :",TRAFFIC_TIME.get())
        print("VEHICLE_PASS_TIME :",VEHICLE_PASS_TIME.get())
        print("CURRENT_TRAFFIC_MODE")

    mybut = Button(root,text = "Submit all variables!", command = submit, padx =20, pady =5, fg='blue',font= heading_2)
    mybut.grid(row=4, column=1)
    #mybut.pack()

    def smart():
        CURRENT_TRAFFIC_MODE = "Smart Mode"
        print("CURRENT_TRAFFIC_MODE:",CURRENT_TRAFFIC_MODE)
        c = ("CURRENT_TRAFFIC_MODE: " + CURRENT_TRAFFIC_MODE)
        myLabel6 = Label(root, text=c, fg='black', font=heading_1)
        myLabel6.grid(row=6, column=0)

    def normal():
        CURRENT_TRAFFIC_MODE = "Normal Mode"
        print("CURRENT_TRAFFIC_MODE:", CURRENT_TRAFFIC_MODE)
        c = ("CURRENT_TRAFFIC_MODE: " + CURRENT_TRAFFIC_MODE)
        myLabel6 = Label(root, text=c, fg='black', font=heading_1)
        myLabel6.grid(row=6, column=0)

    def manual():
        CURRENT_TRAFFIC_MODE = "Manual Mode"
        print("CURRENT_TRAFFIC_MODE:", CURRENT_TRAFFIC_MODE)
        c = ("CURRENT_TRAFFIC_MODE: " + CURRENT_TRAFFIC_MODE)
        myLabel6 = Label(root, text=c, fg='black', font=heading_1)
        myLabel6.grid(row=6, column=0)

    myLabel5 = Label(root, text="", fg='black', font=heading_1)
    myLabel5.grid(row=5, column=0)
    c = ("CURRENT_TRAFFIC_MODE: "+ CURRENT_TRAFFIC_MODE)
    myLabel6 = Label(root, text=c, fg='black', font=heading_1)
    myLabel6.grid(row=6, column=0)

    Modesel_smart = Button(root, text="Smart Mode", command=smart, padx=20, pady=5, fg='red', font=heading_2)
    Modesel_smart.grid(row=8, column=0)

    Modesel_normal = Button(root, text="Normal Mode", command=normal, padx=20, pady=5, fg='red', font=heading_2)
    Modesel_normal.grid(row=8, column=1)

    Modesel_manual = Button(root, text="Manual Mode", command=manual, padx=20, pady=5, fg='red', font=heading_2)
    Modesel_manual.grid(row=8, column=2)


    root.mainloop()

gui(CURRENT_TRAFFIC_MODE)