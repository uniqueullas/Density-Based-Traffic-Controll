"""
Requirment for smart mode
●        Variables with updated density count
●        Calculate delay using
           ○  signalTime =(vehicleCountSignalD)x(timePerVehicle)
           ○  VEHICLE_PASS_TIME = time taken for 1 vehicle to pass the signal [variable]
●        Assign delay correspondingly
"""
import time
import threading
imageCaptureVariable = False

def ledControl(signalTime,road):
    totalSignalTime = (int(round(time.time() + signalTime)))
    prasentTime = (int(round(time.time())))
    print("road:", road)
    while (totalSignalTime > prasentTime):
        time.sleep(1)
        #if((totalSignalTime - prasentTime)<3):
        #r = global imageCaptureVariable
        #print(r)
        prasentTime = (int(round(time.time())))
        print("Elapsing time:", totalSignalTime - prasentTime)
    print("ledControl Over")

def normalMode(road):
    print("nomalMode")
    ledControl(5, road)

    """print("nomalMode")
    if (road < 5):
        ledControl(5, road)
    else:
        if(smartModeFlag):
            smartMode(timePerVehicle=3,vehicleCount=2,road=0)
        else:
            print("running normalMode again..!")"""


def smartMode(timePerVehicle, vehicleCount, road):
    print("smartMode")
    signalTime = (vehicleCount * timePerVehicle)
    ledControl(signalTime, road)

    """if (road < 5):
        ledControl(signalTime,road)
    else:
        if(normalModeFlag):
            normalMOde(road)
        else:
            print("running smartMode again..!")"""


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