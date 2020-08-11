
from tkinter import *
import tkinter.font as tkFont
from PIL import ImageTk,Image

def User_input_GUI():
    CURRENT_TRAFFIC_MODE = "Normal Mode"

    root = Tk()
    root.geometry("601x700")
    root.title("Telaverge Communications")
    root.iconbitmap("TELALOGO.ico")
    title = tkFont.Font(family="impact", size = 30)
    heading_1 = tkFont.Font(family="Lucida Grande", size=10, )
    heading_2 = tkFont.Font(family="Lucida Grande", size=10)

    myLabel1 = Label(root, text="Density", fg = 'black', font=title)
    myLabel1.grid(row=0, column=0)
    myLabel1f = Label(root, text=" Based Smart", fg='black', font=title)
    myLabel1f.grid(row=0, column=1)
    myLabel1l = Label(root, text=" Traffic", fg='black', font=title)
    myLabel1l.grid(row=0, column=2)
    myLabel1l1 = Label(root, text=" Control", fg='black', font=title)
    myLabel1l1.grid(row=0, column=3)

    def login():
        gap_l = Label(root, text="", fg='black', font=heading_1)
        gap_l.grid(row=2, column=1)
        gap_2 = Label(root, text="", fg='black', font=heading_1)
        gap_2.grid(row=3, column=1)

        User_l = Label(root, text="User name", fg='black', font=heading_1)
        User_l.grid(row=5, column=0)
        User = Entry(root, font=heading_1)  # ney
        User.grid(row=5, column=1)

        password_l= Label(root, text="Password", fg='black', font=heading_1)
        password_l.grid(row=6, column=0)
        password= Entry(root, font=heading_1)  # eey
        password.grid(row=6, column=1)

        def check():
            print("user:", User.get())
            print("pass:",password.get())

            if (User.get() != "admin"):
                print("user name not found")
                user_2 = Label(root, text="user id not found", fg='black', font=heading_2)
                user_2.grid(row=7, column=1)
            else:
                if (password.get() != "admin"):
                    print("password worng")
                    password_2 = Label(root, text="worng password", fg='black', font=heading_2)
                    password_2.grid(row=7, column=1)
                else:
                    gap_3 = Label(root, text="", fg='black', font=heading_2)
                    gap_3.grid(row=7, column=1)
                    gap_l.grid_forget()
                    gap_2.grid_forget()
                    User_l.grid_forget()
                    User.grid_forget()
                    password_l.grid_forget()
                    password.grid_forget()
                    loggin.grid_forget()

                    gui(CURRENT_TRAFFIC_MODE)

        loggin = Button(root, text="login", command=check, padx=30, pady=4, fg='blue', font=heading_2)
        #photo = PhotoImage(file="TELALOGO.png")
        #loggin = Button(root, text="login", image=photo, command=check, padx=30, pady=4, fg='blue', font=heading_2)
        loggin.grid(row=8, column=1)
        root.mainloop()


    def gui(CURRENT_TRAFFIC_MODE):
        CURRENT_TRAFFIC_MODE = CURRENT_TRAFFIC_MODE
        myLabel2 = Label(root, text="MINIMUM_VEHICLE", fg='black', font=heading_1)
        myLabel2.grid(row=1, column=0)
        MINIMUM_VEHICLE= Entry(root,font=heading_1)
        MINIMUM_VEHICLE.grid(row=1, column=1)
        myLabel3 = Label(root, text="TRAFFIC_TIME", fg='black', font=heading_1)
        myLabel3.grid(row=2, column=0)
        TRAFFIC_TIME= Entry(root, font=heading_1)
        TRAFFIC_TIME.grid(row=2, column=1)
        myLabel4 = Label(root, text="VEHICLE_PASS_TIME", fg='black', font=heading_1)
        myLabel4.grid(row=3, column=0)
        VEHICLE_PASS_TIME=Entry(root, font=heading_1)
        VEHICLE_PASS_TIME.grid(row=3, column=1)


        def run_this():
            print("this is running")

            myLabel6 = Label(root, text="CURRENT_MODE:", fg='black', font=heading_1)
            myLabel6.grid(row=6, column=0)
            myla = Label(root, text=CURRENT_TRAFFIC_MODE, fg='black', font=heading_1)
            myla.grid(row=6, column=1)
            gap_9 = Label(root, text="", fg='black', font=heading_1)
            gap_9.grid(row=9, column=2)

            myLabei1 = Label(root, text="Side A", fg='black', font=heading_2)
            myLabei1.grid(row=10, column=1)
            my_img1 = Image.open("Shapes.png")
            resized1 = my_img1.resize((100, 100), Image.ANTIALIAS)
            new_pic1 = ImageTk.PhotoImage(resized1)
            SideAL = Label(image=new_pic1)
            SideAL.grid(row=11, column=1)

            myLabei2 = Label(root, text="Side B", fg='black', font=heading_2)
            myLabei2.grid(row=12, column=0)
            my_img2 = Image.open("Shapes.png")
            resized2 = my_img2.resize((100, 100), Image.ANTIALIAS)
            new_pic2 = ImageTk.PhotoImage(resized2)
            SideBL = Label(image=new_pic2)
            SideBL.grid(row=13, column=0)

            gap_12 = Label(root, text="", fg='black', font=heading_1)
            gap_12.grid(row=13, column=1)

            myLabei3 = Label(root, text="Side C", fg='black', font=heading_2)
            myLabei3.grid(row=12, column=2)
            my_img3 = Image.open("Shapes.png")
            resized3 = my_img3.resize((100, 100), Image.ANTIALIAS)
            new_pic3 = ImageTk.PhotoImage(resized3)
            SideCL = Label(image=new_pic3)
            SideCL.grid(row=13, column=2)

            myLabei4 = Label(root, text="Side D", fg='black', font=heading_2)
            myLabei4.grid(row=14, column=1)
            my_img4 = Image.open("Shapes.png")
            resized4 = my_img4.resize((100, 100), Image.ANTIALIAS)
            new_pic4 = ImageTk.PhotoImage(resized4)
            SideDL = Label(image=new_pic4)
            SideDL.grid(row=15, column=1)
            button_quit = Button(root, text="exit", command=root.quit)
            button_quit.grid(row=20, column=1)
            root.mainloop()

        def submit():
            print("MINIMUM_VEHICLE :",MINIMUM_VEHICLE.get())
            print("TRAFFIC_TIME :",TRAFFIC_TIME.get())
            print("VEHICLE_PASS_TIME :",VEHICLE_PASS_TIME.get())
            print("CURRENT_TRAFFIC_MODE")

        mybut = Button(root,text = "Submit all variables!", command = submit, padx =20, pady =5, fg='blue',font= heading_2)
        mybut.grid(row=4, column=1)
        gap_5 = Label(root, text="", fg='black', font=heading_1)
        gap_5.grid(row=5, column=2)

        def auto():
            CURRENT_TRAFFIC_MODE = "Auto Mode  "
            print("CURRENT_MODE:",CURRENT_TRAFFIC_MODE)
            myLabel6 = Label(root, text="CURRENT_MODE:" , fg='black', font=heading_1)
            myLabel6.grid(row=6, column=0)
            myla =  Label(root, text= CURRENT_TRAFFIC_MODE, fg='black', font=heading_1)
            myla.grid(row=6, column=1)
            run_this()

        def manual():
            CURRENT_TRAFFIC_MODE = "Manual Mode"
            print("CURRENT_MODE:", CURRENT_TRAFFIC_MODE)
            myLabel6 = Label(root, text="CURRENT_MODE:", fg='black', font=heading_1)
            myLabel6.grid(row=6, column=0)
            myla = Label(root, text=CURRENT_TRAFFIC_MODE, fg='black', font=heading_1)
            myla.grid(row=6, column=1)

            photoa = Image.open("arrow_up.png")
            resizeda = photoa.resize((96, 96), Image.ANTIALIAS)
            newphotoa = ImageTk.PhotoImage(resizeda)

            photob = Image.open("arrow_left.png")
            resizedb = photob.resize((96, 96), Image.ANTIALIAS)
            newphotob = ImageTk.PhotoImage(resizedb)

            photoc = Image.open("arrow_right.png")
            resizedc = photoc.resize((96, 96), Image.ANTIALIAS)
            newphotoc = ImageTk.PhotoImage(resizedc)

            photod = Image.open("arrow_down.png")
            resizedd = photod.resize((96, 96), Image.ANTIALIAS)
            newphotod = ImageTk.PhotoImage(resizedd)

            arrowa = Button(root, text="up", image=newphotoa, padx=60, pady=60, fg='blue', font=heading_2)
            arrowa.grid(row=11, column=1)
            arrowb = Button(root, text="left", image=newphotob, padx=60, pady=60, fg='blue', font=heading_2)
            arrowb.grid(row=13, column=0)
            arrowc = Button(root, text="right", image=newphotoc, padx=60, pady=60, fg='blue', font=heading_2)
            arrowc.grid(row=13, column=2)
            arrowd = Button(root, text="down", image=newphotod, padx=60, pady=60, fg='blue', font=heading_2)
            arrowd.grid(row=15, column=1)
            root.mainloop()

            # gap_9
            # myLabei1
            #SideAL.grid_forget()
            # myLabei2
            # SideBL
            # myLabei3
            # SideCL
            # myLabei4
            # SideDL

        gap_7 = Label(root, text="", fg='black', font=heading_1)
        gap_7.grid(row=7, column=2)
        Modesel_smart = Button(root, text="Auto Mode", command=auto, padx=20, pady=5, fg='red', font=heading_2)
        Modesel_smart.grid(row=8, column=0)
        Modesel_normal = Button(root, text="Manual Mode", command=manual, padx=20, pady=5, fg='red', font=heading_2)
        Modesel_normal.grid(row=8, column=1)
        run_this()
    login()