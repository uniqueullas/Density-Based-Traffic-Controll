from User_input_GUI import *
from smartMode import *
from PIL import ImageTk,Image
from base_file import *

#image = density_calculation()
#User_input_GUI()
vehicleCount = 5; vehicleCountThreshold = 3 #sideA

vehicleCount = 1; vehicleCountThreshold = 3 #sideB

timePerVehicle = 3

smartModeFlag = False
normalModeFlag = True


#while(1):

for road in range(1, 4):
    if(vehicleCount > vehicleCountThreshold):
        smartMode(timePerVehicle, vehicleCount, road)
    else:
        normalMode(road)
    print("--------------------------------")
