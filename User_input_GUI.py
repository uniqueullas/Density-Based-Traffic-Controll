"""
img=cv2.imread("Shapes.png")
dimension=(100,100)
resized=cv2.resize(img,dimension)
"""

from tkinter import *
import tkinter.font as tkFont

def user_input_GUI():
    current_traffic_mode = "Normal Mode"
    root = Tk()
    #root.geometry("1000x200")
    root.title("Telaverge Communications")
    root.iconbitmap("TELALOGO.ico")
    title = tkFont.Font(family="impact", size=50)
    score = tkFont.Font(family="impact", size=40, )
    heading_2 = tkFont.Font(family="Lucida Grande", size=10)

    Label(root, text="Density", fg='black', font=title).grid(row=0, column=0,sticky=E+W)
    Label(root, text="Based", fg='black', font=title).grid(row=0, column=1,sticky=E+W)
    Label(root, text="Smart", fg='black', font=title).grid(row=0, column=2,sticky=E+W)
    Label(root, text="Traffic", fg='black', font=title).grid(row=0, column=3,sticky=E+W)
    Label(root, text="Control", fg='black', font=title).grid(row=0, column=4,sticky=E+W)

    """sb = Scrollbar(root)
    sb.grid(row=0, column=6, columnspan=1, rowspan=5, sticky=E+W)
    mylist = Listbox(root, yscrollcommand=sb.set)
    for line in range(30):
        mylist.insert(END, "Number " + str(line))
    mylist.grid(row=0, column=5, columnspan=1, rowspan=20, sticky=E+S)
    sb.config(command=mylist.yview)"""

    def login():
        Label(root, text="", fg='black', font=heading_2).grid(row=2, column=1)  # gap
        Label(root, text="", fg='black', font=heading_2).grid(row=3, column=1)  # gap

        user_asked = Label(root, text="user name", fg='black', font=heading_2)
        user_asked.grid(row=5, column=0)
        user_typed = Entry(root, font=heading_2)
        user_typed.grid(row=5, column=1)

        password_asked = Label(root, text="Password", fg='black', font=heading_2)
        password_asked.grid(row=6, column=0)
        password_typed = Entry(root, font=heading_2)
        password_typed.grid(row=6, column=1)

        def check():
            if user_typed.get() != "admin":
                Label(root, text="user id not found", fg='black', font=heading_2).grid(row=7, column=1, sticky=E)
            else:
                if password_typed.get() != "admin":
                    Label(root, text="worng password", fg='black', font=heading_2).grid(row=7, column=1, sticky=E)
                else:
                    Label(root, text="                        ", fg='black', font=heading_2).grid(row=7, column=1, sticky=E)
                    user_asked.grid_forget()
                    password_asked.grid_forget()
                    password_typed.grid_forget()
                    user_typed.grid_forget()
                    loggin_button.grid_forget()
                    second_window(current_traffic_mode)

        Label(root, text="  ", fg='black', font=heading_2).grid(row=7, column=2)
        loggin_button = Button(root, text="login", command=check, padx=30, pady=4, fg='blue', font=heading_2)
        loggin_button.grid(row=8, column=1)
        root.mainloop()

    def second_window(current_traffic_mode):
        Label(root, text="").grid(row=50, column=3)
        Label(root, text="Vehicle Threshold:", fg='black', font=heading_2).grid(row=1, column=0,sticky=E)
        minium_vehicle_typed= Entry(root,font=heading_2)
        minium_vehicle_typed.grid(row=1, column=1,padx=1, pady=1,sticky=W)
        up = PhotoImage(file="up.png")
        down = PhotoImage(file="down.png")
        Button(root, image=up, padx=8, pady=3, repeatinterval=5000, cursor='hand2', activebackground='red',)\
            .grid(row=1, column=1,padx=1, pady=1,sticky=E)
        Button(root, image=down, padx=8, pady=3, repeatinterval=5000, cursor='hand2', activebackground='red', ) \
            .grid(row=1, column=2, padx=1, pady=1, sticky=W)
        Label(root, text="Number of Lanes:", fg='black', font=heading_2).grid(row=2, column=0,sticky=E)
        traffic_time_typed= Entry(root, font=heading_2)
        traffic_time_typed.grid(row=2, column=1,padx=1, pady=1,sticky=W)
        Button(root, image=up, padx=8, pady=3, repeatinterval=5000, cursor='hand2', activebackground='red', ) \
            .grid(row=2, column=1, padx=1, pady=1, sticky=E)
        Button(root, image=down, padx=8, pady=3, repeatinterval=5000, cursor='hand2', activebackground='red', ) \
            .grid(row=2, column=2, padx=1, pady=1, sticky=W)
        Label(root, text="Vehicle Pass Time:", fg='black', font=heading_2).grid(row=3, column=0,sticky=E)
        vehicle_pass_time_typed=Entry(root, font=heading_2)
        vehicle_pass_time_typed.grid(row=3, column=1, padx=1, pady=1,sticky=W)
        Button(root, image=up, padx=8, pady=3, repeatinterval=5000, cursor='hand2', activebackground='red', ) \
            .grid(row=3, column=1, padx=1, pady=1, sticky=E)
        Button(root, image=down, padx=8, pady=3, repeatinterval=5000, cursor='hand2', activebackground='red', ) \
            .grid(row=3, column=2, padx=1, pady=1, sticky=W)

        def run_this():
            Label(root, text="Current Mode:", fg='black', font=heading_2).grid(row=6, column=0)
            Label(root, text=current_traffic_mode, fg='black', font=heading_2).grid(row=6, column=1)
            Label(root, text="", fg='black', font=heading_2).grid(row=9, column=1)
            Label(root, text="Side A", fg='black', font=heading_2).grid(row=10, column=0)
            Label(root, text="Side B", fg='black', font=heading_2).grid(row=10, column=1)
            Label(root, text="Side C", fg='black', font=heading_2).grid(row=10, column=2)
            Label(root, text="Side D", fg='black', font=heading_2).grid(row=10, column=3)
            Label(root, text="Elapsing Time", fg='black', font=heading_2).grid(row=10, column=4)

            psidea = PhotoImage(file="Shapes_resized.png")
            Label(root, image=psidea, height=120, width=100, compound=TOP, bg='black').grid(row=11, column=0)
            psideb = PhotoImage(file="Shapes_resized.png")
            Label(root, image=psideb, height=120, width=100, compound=TOP, bg='black').grid(row=11, column=1)
            psidec = PhotoImage(file="Shapes_resized.png")
            Label(root, image=psidec, height=120, width=100, compound=TOP, bg='black').grid(row=11, column=2)
            psided = PhotoImage(file="Shapes_resized.png")
            Label(root, image=psided, height=120, width=100, compound=TOP, bg='black').grid(row=11, column=3)
            elapsing = "99"
            Label(root, text=elapsing, height=1, width=4, bg='yellow',fg='red', font=score).grid(row=11, column=4)
            root.mainloop()

        def submit():
            Label(root, text=minium_vehicle_typed.get(), fg='black', font=heading_2).grid(row=1, column=2)
            Label(root, text=traffic_time_typed.get(), fg='black', font=heading_2).grid(row=2, column=2)
            Label(root, text=vehicle_pass_time_typed.get(), fg='black', font=heading_2).grid(row=3, column=2)

        Button(root, text="Submit all variables!", command=submit, padx=8, pady=3, fg='blue',
               state='normal', repeatinterval=500, cursor='hand2',
               activebackground='blue',font= heading_2).grid(row=4, column=1,padx=1, pady=1,sticky=W)
        Label(root, text="", fg='black', font=heading_2).grid(row=5, column=2)

        def auto():
            current_traffic_mode = "Auto Mode  "
            Label(root, text="Current Mode:", fg='black', font=heading_2).grid(row=6, column=0)
            Label(root, text=current_traffic_mode, fg='black', font=heading_2).grid(row=6, column=1)
            run_this()

        def manual():
            current_traffic_mode = "Manual Mode"
            Label(root, text="", height=1, width=15).grid(row=10, column=4)
            Label(root, text="", height=10, width=20).grid(row=11, column=4)
            Button(root, text="Submit all variables!", padx=8, pady=3, fg='blue',
                   state='disabled', repeatinterval=500, cursor='hand2',
                   activebackground='blue', font=heading_2).grid(row=4, column=1, padx=1, pady=1, sticky=W)
            Label(root, text="", fg='black', font=heading_2).grid(row=5, column=2)
            Label(root, text="Current Mode:", fg='black', font=heading_2).grid(row=6, column=0)
            Label(root, text=current_traffic_mode, fg='black', font=heading_2).grid(row=6, column=1)
            sidea = PhotoImage(file="arrow_left.png")
            sideb = PhotoImage(file="arrow_up.png")
            sidec = PhotoImage(file="arrow_down.png")
            sided = PhotoImage(file="arrow_right.png")
            Button(root, text="Click", image=sidea, height=120, width=100, compound=TOP, bg='white').grid(row=11,
                                                                                                          column=0)
            Button(root, text="Click", image=sideb, height=120, width=100, compound=TOP, bg='white').grid(row=11,
                                                                                                          column=1)
            Button(root, text="Click", image=sidec, height=120, width=100, compound=TOP, bg='white').grid(row=11,
                                                                                                          column=2)
            Button(root, text="Click", image=sided, height=120, width=100, compound=TOP, bg='white').grid(row=11,
                                                                                                          column=3)
            root.mainloop()

        Label(root, text="", fg='black', font=heading_2).grid(row=7, column=2)
        Button(root, text="Auto Mode", command=auto, padx=20, pady=5, fg='red', font=heading_2).grid(row=8, column=0)
        Button(root, text="Manual Mode", command=manual, padx=20, pady=5, fg='red', font=heading_2).grid(row=8, column=1)
        run_this()
    login()
    #second_window(current_traffic_mode)


user_input_GUI()