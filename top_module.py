from User_input_GUI import *
from smartMode import *
from PIL import ImageTk,Image
from base_file import *


#image = density_calculation()
#User_input_GUI()
#vehicleCount = 1; vehicleCountThreshold = 3 #sideB


time_per_vehicle = 3
vehicle_count_threshold = 3
while 1:
    for road in range(1, 5):
        print("vehicle_count:", vehicle_count[road], end='')
        if vehicle_count[road] > vehicle_count_threshold:
            smart_mode(time_per_vehicle, vehicle_count[road], road)
        else:
            normal_mode(road)
    print("Finished Iteration")
