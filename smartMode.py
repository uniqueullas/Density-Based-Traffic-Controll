"""
Requirment for smart mode
●        Variables with updated density count
●        Calculate delay using
           ○  signalTime =(vehicleCountSignalD)x(timePerVehicle)
           ○  VEHICLE_PASS_TIME = time taken for 1 vehicle to pass the signal [variable]
●        Assign delay correspondingly
"""
import time


def ledControl(signalTime,road):
    print("led function called")
    print("signalTime:",signalTime)
    print("road:", road)
    print("delay started..!")
    time.sleep(signalTime)
    print("ledControl Over")

def normalMode(road):
    print("this is nomalMode")
    if (road < 4):
        ledControl(5, road)
    else:
        if(smartModeFlag):
            smartMode(timePerVehicle=3,vehicleCount=2,road=0)
        else:
            print("running normalMode again..!")

def smartMode(timePerVehicle, vehicleCount, road):
    print("this is smartMode")
    signalTime = (vehicleCount * timePerVehicle)
    if (road <= 4):
        ledControl(signalTime,road)
    else:
        if(normalModeFlag):
            normalMOde(road)
        else:
            print("running smartMode again..!")

