"""Requirement for smart mode
● Variables with updated density count
● Calculate delay using
  ○  signal_time =(vehicle_countSignalD)x(time_per_vehicle)
  ○  VEHICLE_PASS_TIME = time taken for 1 vehicle to pass the signal [variable]
● Assign delay correspondingly"""

from base_file import *
import time
import threading
image_capture_variable = True
vehicle_count = [0, 1, 5, 0, 0]
ele_time_disp = 0
road_led = 0
st_auto = False

time_per_vehicle = 0
vehicle_threshold = 0
normal_delay = 0


def stop_auto():
    global st_auto
    st_auto = True


def get_elapsing_time():
    global ele_time_disp
    global road_led
    return ele_time_disp, road_led


def mode_selection():
    global st_auto
    st_auto = False
    for road in range(1, 5):
        print("vehicle_count:", vehicle_count[road], end='') #vehicle_count[] list is declared in smartMode.py
        if vehicle_count[road] > vehicle_threshold:
            smart_mode(time_per_vehicle, vehicle_count[road], road)
        else:
            normal_mode(road)
        time.sleep(1)
        print("Finished Iteration")


def led_control(signal_time, road):
    global road_led
    road_led = road
    print("-----road+:", road_led)
    total_signal_time = (int(round(time.time() + signal_time)))
    present_time = (int(round(time.time())))
    print_time = (int(round(time.time())))
    while total_signal_time > present_time or total_signal_time == present_time:
        global st_auto
        if st_auto:
            break
        if (total_signal_time - present_time) < 3:
            global image_capture_variable
            image_capture_variable = False
        else:
            image_capture_variable = True
        current_time = (int(round(time.time())))
        if current_time == print_time:
            global ele_time_disp
            print_time = (int(round(time.time()+1)))
            ele_time_disp = total_signal_time - present_time
            print("Elapsing time:", ele_time_disp)
            present_time = (int(round(time.time())))
    print("--------------------led control over")


def normal_mode(road_normal):
    global normal_delay
    print("--------------------normal mode--------------", end='')
    nt1 = threading.Thread(target=led_control, args=(normal_delay, road_normal,))
    nt2 = threading.Thread(target=img_capture, args=())
    nt1.start()
    nt2.start()
    nt1.join()
    nt2.join()


def smart_mode(time_per_vehicle_smart, vehicle_count_smart, road_smart):
    print("---------------------smart_mode----------------", end='')
    signal_time = (vehicle_count_smart * time_per_vehicle_smart)
    stt1 = threading.Thread(target=led_control, args=(signal_time, road_smart,))
    stt2 = threading.Thread(target=img_capture, args=())
    stt1.start()
    stt2.start()
    stt1.join()
    stt2.join()


def img_capture():
    global image_capture_variable
    while image_capture_variable:
        pass
