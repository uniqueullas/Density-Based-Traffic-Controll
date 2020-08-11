from User_input_GUI import *
from smartMode import *
from PIL import ImageTk,Image
from base_file import *

#image = density_calculation()
#User_input_GUI()
#vehicleCount = 1; vehicleCountThreshold = 3 #sideB

imageCaptureVariable = False
timePerVehicle = 3
vehicleCountThreshold = 3
vehicleCount = [0,5,0,6,1]

road = 1
for road in range(1, 5):
    print("vehicleCount:", vehicleCount[road])
    if(vehicleCount[road] > vehicleCountThreshold):
        smartMode(timePerVehicle, vehicleCount[road], road)
    else:
        normalMode(road)
    print("--------------------------------")
