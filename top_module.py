from User_input_GUI import *
from smartMode import *
import threading
from PIL import ImageTk,Image
from base_file import *


#image = density_calculation()

#vehicleCount = 1; vehicleCountThreshold = 3 #sideB


time_per_vehicle = 3
vehicle_count_threshold = 3


def mode_selection():
    while 1:
        for road in range(1, 5):
            print("vehicle_count:", vehicle_count[road], end='') #vehicle_count[] list is declared in smartMode.py
            if vehicle_count[road] > vehicle_count_threshold:
                smart_mode(time_per_vehicle, vehicle_count[road], road)
            else:
                normal_mode(road)
        print("Finished Iteration")
mode_selection()

"""gui = threading.Thread(target=User_input_GUI, args=())
cal = threading.Thread(target=doso, args=())
gui.start()
cal.start()
"""