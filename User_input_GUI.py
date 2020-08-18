"""img=cv2.imread("Shapes.png")
dimension=(100,100)
resized=cv2.resize(img,dimension)

14-08-2020
Vehicle Threshold
Vehicle Per Time
Normal delay"""
from tkinter import *
import tkinter.font as tkFont
from smartMode import *
from base_file import *
import smartMode


show_elapsing_time = False
manual_a = "STOP"
manual_b = "STOP"
manual_c = "STOP"
manual_d = "STOP"
manual_road1 = "red"
manual_road2 = "red"
manual_road3 = "red"
manual_road4 = "red"


def login():
    Label(root, text="", fg='black', font=heading_2).grid(row=2, column=1)
    Label(root, text="", fg='black', font=heading_2).grid(row=3, column=1)
    user_asked = Label(root, text="User Name", fg='black', font=heading_2)
    user_asked.grid(row=5, column=0)
    user_typed = Entry(root, font=heading_2)
    user_typed.grid(row=5, column=1)
    password_asked = Label(root, text="Password", fg='black', font=heading_2)
    password_asked.grid(row=6, column=0)
    password_typed = Entry(root, font=heading_2)
    password_typed.grid(row=6, column=1)
    telaverge_logo = PhotoImage(file="TELALOGO.png")
    telaverge = Label(root, image=telaverge_logo, height=80, width=500, compound=TOP)
    telaverge.grid(row=5, column=2, columnspan=3, rowspan=3)

    def check():
        if user_typed.get() != "":
            Label(root, text="user id not found", fg='black', font=heading_2).grid(row=7, column=1, sticky=E)
        else:
            if password_typed.get() != "":
                Label(root, text="wrong password", fg='black', font=heading_2).grid(row=7, column=1, sticky=E)
            else:
                Label(root, text="                        ", fg='black', font=heading_2).grid(row=7, column=1, sticky=E)
                telaverge.grid_forget()
                user_asked.grid_forget()
                password_asked.grid_forget()
                password_typed.grid_forget()
                user_typed.grid_forget()
                loggin_button.grid_forget()
                guith_1 = threading.Thread(target=second_window, args=(current_traffic_mode,))
                guith_2 = threading.Thread(target=update_every_sec)
                guith_1.start()
                guith_2.start()

    loggin_button = Button(root, text="Login", command=check, padx=30, pady=4, fg='blue', font=heading_2)
    loggin_button.grid(row=8, column=1)
    Button(root, text="X", command=quit, padx=1, pady=1, fg='white', bg='red',
           state='normal', repeatinterval=500, cursor='hand2',
           activebackground='black', font=heading_2).grid(row=1, column=4, padx=1, pady=1, sticky=E + N)
    Label(root, text="  ").grid(row=9, column=2)
    root.mainloop()


def update_every_sec():
    global show_elapsing_time
    elapsing, road = get_elapsing_time()
    if road == 1:
        road1 = 'green'; road2 = 'red'; road3 = 'red'; road4 = 'red'
        elapsing_time1 = elapsing; elapsing_time2 = (elapsing+1); elapsing_time3 = "--"; elapsing_time4 = "--"
    elif road == 2:
        road1 = 'red'; road2 = 'green'; road3 = 'red'; road4 = 'red'
        elapsing_time1 = "--"; elapsing_time2 = elapsing; elapsing_time3 = (elapsing+1); elapsing_time4 = "--"
    elif road == 3:
        road1 = 'red'; road2 = 'red'; road3 = 'green'; road4 = 'red'
        elapsing_time1 = "--"; elapsing_time2 = "--"; elapsing_time3 = elapsing; elapsing_time4 = (elapsing+1)
    elif road == 4:
        road1 = 'red'; road2 = 'red'; road3 = 'red'; road4 = 'green'
        elapsing_time1 = (elapsing+1); elapsing_time2 = "--"; elapsing_time3 = "--"; elapsing_time4 = elapsing
    else:
        road2 = 'black'; road3 = 'black'; road1 = 'black'; road4 = 'black'
        elapsing_time1 = "--"; elapsing_time2 = "--"; elapsing_time3 = "--"; elapsing_time4 = "--"
    Label(root, text=smartMode.vehicle_threshold, fg='black', font=heading_2).grid(row=1, column=1, sticky=W)
    Label(root, text=smartMode.time_per_vehicle, fg='black', font=heading_2).grid(row=2, column=1, sticky=W)
    Label(root, text=smartMode.normal_delay, fg='black', font=heading_2).grid(row=3, column=1, sticky=W)
    timeObj = time.localtime(time.time())
    c_time = str('Time Stamp:%d/%d/%d %d:%d:%d' % (timeObj.tm_mday, timeObj.tm_mon, timeObj.tm_year,
                                                   timeObj.tm_hour, timeObj.tm_min, timeObj.tm_sec))
    Label(root, text=c_time, fg='black', font=heading_2).grid(row=8, column=2, columnspan=2)
    if show_elapsing_time:
        et_1 = Label(root, text=elapsing_time1, height=1, width=4, bg='yellow', fg=road1, font=score)
        et_2 = Label(root, text=elapsing_time2, height=1, width=4, bg='yellow', fg=road2, font=score)
        et_3 = Label(root, text=elapsing_time3, height=1, width=4, bg='yellow', fg=road3, font=score)
        et_4 = Label(root, text=elapsing_time4, height=1, width=4, bg='yellow', fg=road4, font=score)
    else:
        global manual_a, manual_b, manual_c, manual_d, manual_road1, manual_road2, manual_road3, manual_road4
        et_1 = Label(root, text=manual_a, height=1, width=4, bg='yellow', fg=manual_road1, font=score)
        et_2 = Label(root, text=manual_b, height=1, width=4, bg='yellow', fg=manual_road2, font=score)
        et_3 = Label(root, text=manual_c, height=1, width=4, bg='yellow', fg=manual_road3, font=score)
        et_4 = Label(root, text=manual_d, height=1, width=4, bg='yellow', fg=manual_road4, font=score)
    Label(root, text="", height=1, width=15).grid(row=10, column=4)
    Label(root, text="", height=1, width=15).grid(row=12, column=0)
    et_1.grid(row=13, column=0)
    et_2.grid(row=13, column=1)
    et_3.grid(row=13, column=2)
    et_4.grid(row=13, column=3)
    root.after(1000, update_every_sec)


def second_window(current_traffic_mode):
    Label(root, text="").grid(row=50, column=3)
    Label(root, text="Vehicle Threshold:", fg='black', font=heading_2).grid(row=1, column=0,sticky=E)
    vehicle_threshold_typed = Entry(root, font=heading_2)
    vehicle_threshold_typed.grid(row=1, column=1, padx=2, pady=1, sticky=E)
    Label(root, text="Time Per Vehicle:", fg='black', font=heading_2).grid(row=2, column=0,sticky=E)
    time_per_vehicle_typed = Entry(root, font=heading_2)
    time_per_vehicle_typed.grid(row=2, column=1, padx=1, pady=1, sticky=E)
    Label(root, text="Normal Delay:", fg='black', font=heading_2).grid(row=3, column=0,sticky=E)
    normal_delay_typed = Entry(root, font=heading_2)
    normal_delay_typed.grid(row=3, column=1, padx=1, pady=1, sticky=E)
    Button(root, text="Auto Mode", command=auto_smart, padx=20, pady=5, fg='red', font=heading_2).grid(row=8, column=0)
    Button(root, text="Manual Mode", command=manual, padx=20, pady=5, fg='red', font=heading_2).grid(row=8, column=1)
    Label(root, text="  ", fg='black', font=heading_2).grid(row=20, column=0)
    Label(root, text="Current Mode:", fg='black', font=heading_2).grid(row=6, column=0, sticky=E)
    Label(root, text=current_traffic_mode, fg='black', font=heading_2).grid(row=6, column=1, sticky=W)

    def incmv():
        smartMode.vehicle_threshold = smartMode.vehicle_threshold + 1

    def decmv():
        smartMode.vehicle_threshold = smartMode.vehicle_threshold - 1

    def inctt():
        smartMode.time_per_vehicle = smartMode.time_per_vehicle + 1

    def dectt():
        smartMode.time_per_vehicle = smartMode.time_per_vehicle - 1

    def incvpt():
        smartMode.normal_delay = smartMode.normal_delay + 1

    def decvpt():
        smartMode.normal_delay = smartMode.normal_delay - 1

    def submit():
        smartMode.vehicle_threshold = int(vehicle_threshold_typed.get())
        smartMode.time_per_vehicle = int(time_per_vehicle_typed.get())
        smartMode.normal_delay = int(normal_delay_typed.get())
    Button(root, text="Submit All Variables!", command=submit, padx=8, pady=3, fg='blue',
           state='normal', repeatinterval=500, cursor='hand2',
           activebackground='black',font= heading_2).grid(row=4, column=1,padx=1, pady=1,sticky=E)
    Button(root,text="+", command=incmv, padx=1, pady=1, fg='black',
           state='normal', repeatinterval=500, cursor='hand2',
           activebackground='red', font=heading_2).grid(row=1, column=1, padx=1, pady=1, sticky=E)
    Button(root, text="-", command=decmv, fg='black',
           state='normal', repeatinterval=500, cursor='hand2',
           activebackground='blue', font=heading_2).grid(row=1, column=2, padx=1, pady=1, sticky=W)
    Button(root, text="+", command=inctt, padx=1, pady=1, fg='black',
           state='normal', repeatinterval=500, cursor='hand2',
           activebackground='red', font=heading_2).grid(row=2, column=1, padx=1, pady=1, sticky=E)
    Button(root, text="-", command=dectt, fg='black',
           state='normal', repeatinterval=500, cursor='hand2',
           activebackground='blue', font=heading_2).grid(row=2, column=2, padx=1, pady=1, sticky=W)
    Button(root, text="+", command=incvpt, padx=1, pady=1, fg='black',
           state='normal', repeatinterval=500, cursor='hand2',
           activebackground='red', font=heading_2).grid(row=3, column=1, padx=1, pady=1, sticky=E)
    Button(root, text="-", command=decvpt, fg='black',
           state='normal', repeatinterval=500, cursor='hand2',
           activebackground='blue', font=heading_2).grid(row=3, column=2, padx=1, pady=1, sticky=W)
    Label(root, text="", fg='black', font=heading_2).grid(row=5, column=2)


def auto_smart():
    th1 = threading.Thread(target=auto)
    th2 = threading.Thread(target=mode_selection)
    th1.start()
    th2.start()


def auto():
    global current_traffic_mode
    current_traffic_mode = "Auto Mode                  "
    global show_elapsing_time
    show_elapsing_time = True
    Label(root, text="", fg='black', font=heading_2).grid(row=5, column=2)
    Label(root, text="Current Mode:", fg='black', font=heading_2).grid(row=6, column=0, sticky=E)
    Label(root, text=current_traffic_mode, fg='black', font=heading_2).grid(row=6, column=1, sticky=W)
    Label(root, text="", fg='black', font=heading_2).grid(row=9, column=1)
    img, a, b = density_calculation()
    txta = "Side_A:", str(a)
    #txta = str("Side_A:", a)
    Label(root, text=txta, fg='black', font=heading_2).grid(row=10, column=0)
    Label(root, text="Side_B", fg='black', font=heading_2).grid(row=10, column=1)
    Label(root, text="Side_C", fg='black', font=heading_2).grid(row=10, column=2)
    Label(root, text="Side_D", fg='black', font=heading_2).grid(row=10, column=3)
    psidea = PhotoImage(file="Shapes_resized.png")
    psideb = PhotoImage(file="Shapes_resized.png")
    psidec = PhotoImage(file="Shapes_resized.png")
    psided = PhotoImage(file="Shapes_resized.png")
    Label(root, image=psidea, height=120, width=100).grid(row=11, column=0)
    Label(root, image=psideb, height=120, width=100).grid(row=11, column=1)
    Label(root, image=psidec, height=120, width=100).grid(row=11, column=2)
    Label(root, image=psided, height=120, width=100).grid(row=11, column=3)
    Button(root, text="X", command=stop_auto, padx=1, pady=1, fg='white', bg='red',
           state='normal', repeatinterval=500, cursor='hand2',
           activebackground='black', font=heading_2).grid(row=1, column=4, padx=1, pady=1, sticky=E + N)
    #root.mainloop()
    global st_auto
    while ~st_auto:
        pass


def manual():
    stop_auto()
    current_traffic_mode = "Manual Mode              "
    global show_elapsing_time
    show_elapsing_time = False
    global manual_a, manual_b, manual_c, manual_d, manual_road1, manual_road2, manual_road3, manual_road4
    manual_a = "STOP"; manual_b = "STOP"; manual_c = "STOP"; manual_d = "STOP"
    manual_road1 = "red"; manual_road2 = "red"; manual_road3 = "red"; manual_road4 = "red"
    Label(root, text="", fg='black', font=heading_2).grid(row=5, column=2)
    Label(root, text="Current Mode:", fg='black', font=heading_2).grid(row=6, column=0, sticky=E)
    Label(root, text=current_traffic_mode, fg='black', font=heading_2).grid(row=6, column=1, sticky=W)

    def fsidea():
        global manual_a, manual_b, manual_c, manual_d, manual_road1, manual_road2, manual_road3, manual_road4
        manual_a = "GO!"; manual_b = "STOP"; manual_c = "STOP"; manual_d = "STOP"
        manual_road1 = "green"; manual_road2 = "red"; manual_road3 = "red"; manual_road4 = "red"
        
    def fsideb():
        global manual_a, manual_b, manual_c, manual_d, manual_road1, manual_road2, manual_road3, manual_road4
        manual_a = "STOP"; manual_b = "GO!"; manual_c = "STOP"; manual_d = "STOP"
        manual_road1 = "red"; manual_road2 = "green"; manual_road3 = "red"; manual_road4 = "red"
        
    def fsidec():
        global manual_a, manual_b, manual_c, manual_d, manual_road1, manual_road2, manual_road3, manual_road4
        manual_a = "STOP"; manual_b = "STOP"; manual_c = "GO!"; manual_d = "STOP"
        manual_road1 = "red"; manual_road2 = "red"; manual_road3 = "green"; manual_road4 = "red"
        
    def fsided():
        global manual_a, manual_b, manual_c, manual_d, manual_road1, manual_road2, manual_road3, manual_road4
        manual_a = "STOP"; manual_b = "STOP"; manual_c = "STOP"; manual_d = "GO!"
        manual_road1 = "red"; manual_road2 = "red"; manual_road3 = "red"; manual_road4 = "green"

    sidea = PhotoImage(file="arrow_left.png")
    sideb = PhotoImage(file="arrow_up.png")
    sidec = PhotoImage(file="arrow_down.png")
    sided = PhotoImage(file="arrow_right.png")
    Label(root, text="Side A", fg='black', font=heading_2).grid(row=10, column=0)
    Label(root, text="Side B", fg='black', font=heading_2).grid(row=10, column=1)
    Label(root, text="Side C", fg='black', font=heading_2).grid(row=10, column=2)
    Label(root, text="Side D", fg='black', font=heading_2).grid(row=10, column=3)
    Button(root, text="Click", image=sidea, command=fsidea, height=120, width=100, compound=TOP, bg='white').grid(row=11, column=0)
    Button(root, text="Click", image=sideb, command=fsideb, height=120, width=100, compound=TOP, bg='white').grid(row=11, column=1)
    Button(root, text="Click", image=sidec, command=fsidec, height=120, width=100, compound=TOP, bg='white').grid(row=11, column=2)
    Button(root, text="Click", image=sided, command=fsided, height=120, width=100, compound=TOP, bg='white').grid(row=11, column=3)
    root.mainloop()

current_traffic_mode = "Click any mode to start"
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
Label(root, text="", fg='black', font=heading_2).grid(row=7, column=2)
login()
root.mainloop()
