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


def led_control(signal_time, road_led):
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
            print("Elapsing time:", total_signal_time - present_time)
            present_time = (int(round(time.time())))
    print("--------------------led control over")


def normal_mode(road_normal):
    print("--------------------normal mode--------------", end='')
    nt1 = threading.Thread(target=led_control, args=(5, road_normal,))
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
