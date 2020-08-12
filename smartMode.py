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
imageCaptureVariable = True
timePerVehicle = 3
vehicleCountThreshold = 3
vehicleCount = [0, 5]


def ledControl(signalTime, road):
    print("led function called----------", end='')
    print("road:", road)
    totalSignalTime = (int(round(time.time() + signalTime)))
    prasentTime = (int(round(time.time())))
    printTime = (int(round(time.time())))
    while totalSignalTime > prasentTime:
        if (totalSignalTime - prasentTime)<3:
            global imageCaptureVariable
            imageCaptureVariable = False
        else:
            imageCaptureVariable = True
        currentTime = (int(round(time.time())))
        if currentTime == printTime:
            printTime = (int(round(time.time()+1)))
            print("Elapsing time:", totalSignalTime - prasentTime)
            prasentTime = (int(round(time.time())))
    print("-----------------------------------------------------------------------------led control over")


def normalMode(road):
    print("-----normal mode-----", end='')
    nt1 = threading.Thread(target=ledControl, args=(5, road,))
    nt2 = threading.Thread(target=img_capture, args=())
    nt1.start()
    nt2.start()
    nt2.join()


def smartMode(timePerVehicle, vehicleCount, road):
    print("-----smartMode-----", end='')
    signalTime = (vehicleCount * timePerVehicle)
    st1 = threading.Thread(target=ledControl, args=(signalTime, road,))
    st2 = threading.Thread(target=img_capture, args=())
    st1.start()
    st2.start()
    st1.join()
    st2.join()


def img_capture():
    global imageCaptureVariable
    while imageCaptureVariable:
        pass
    it = (input("-------------------------vehicleCount:"))
    vehicleCount.append(int(it))


while 1:
    for road in range(1, 5):
        print("vehicleCount:", vehicleCount[road], end='')
        if vehicleCount[road] > vehicleCountThreshold:
            smartMode(timePerVehicle, vehicleCount[road], road)
            print("finshed itration")
        else:
            normalMode(road)
