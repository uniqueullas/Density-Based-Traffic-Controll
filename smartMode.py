"""Requirement for smart mode
● Variables with updated density count
● Calculate delay using
  ○  signal_time =(vehicle_countSignalD)x(time_per_vehicle)
  ○  VEHICLE_PASS_TIME = time taken for 1 vehicle to pass the signal [variable]
● Assign delay correspondingly"""
import time
import threading
image_capture_variable = True
vehicle_count = [0, 1]
time_per_vehicle = 3
vehicle_count_threshold = 3
ele_time = 0

def mode_selection():
    for road in range(1, 5):
        print("vehicle_count:", vehicle_count[road], end='') #vehicle_count[] list is declared in smartMode.py
        if vehicle_count[road] > vehicle_count_threshold:
            smart_mode(time_per_vehicle, vehicle_count[road], road)
        else:
            normal_mode(road)
        print("Finished Iteration")

def ele(signal_time):
    total_signal_time = (int(round(time.time() + signal_time)))
    present_time = (int(round(time.time())))
    print_time = (int(round(time.time())))
    while total_signal_time > present_time:
        current_time = (int(round(time.time())))
        if current_time == print_time:
            print_time = (int(round(time.time()+1)))
            ele_timee = total_signal_time - present_time
            present_time = (int(round(time.time())))
    r=1
    return ele_timee, r

def get_elapsing_time():
    timeObj = time.localtime(time.time())
    elapsing = timeObj.tm_sec
    road = 1
    return elapsing, road

def led_control(signal_time, road_led):
    global ele_time
    print("-----road:", road_led)
    total_signal_time = (int(round(time.time() + signal_time)))
    present_time = (int(round(time.time())))
    print_time = (int(round(time.time())))
    while total_signal_time > present_time:
        if (total_signal_time - present_time) < 3:
            global image_capture_variable
            image_capture_variable = False
        else:
            image_capture_variable = True
        current_time = (int(round(time.time())))
        if current_time == print_time:
            print_time = (int(round(time.time()+1)))
            print("")
            ele_time = total_signal_time - present_time
            print("Elapsing time:", ele_time)
            present_time = (int(round(time.time())))
    print("--------------------led control over")


def normal_mode(road_normal):
    print("--------------------normal mode--------------", end='')
    nt1 = threading.Thread(target=led_control, args=(15, road_normal,))
    nt2 = threading.Thread(target=img_capture, args=())
    nt1.start()
    nt2.start()
    nt1.join()
    nt2.join()


def smart_mode(time_per_vehicle_smart, vehicle_count_smart, road_smart):
    print("---------------------smart_mode----------------", end='')
    signal_time = (vehicle_count_smart * time_per_vehicle_smart)
    st1 = threading.Thread(target=led_control, args=(signal_time, road_smart,))
    st2 = threading.Thread(target=img_capture, args=())
    st1.start()
    st2.start()
    st1.join()
    st2.join()


def img_capture():
    global image_capture_variable
    while image_capture_variable:
        pass
    it = (input("-----vehicle_count:"))
    print("", end='')
    vehicle_count.append(int(it))

#mode_selection()