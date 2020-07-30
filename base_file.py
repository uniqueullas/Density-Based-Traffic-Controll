import cv2
import numpy as np
y=1
idx = 0

def getContours_1(img,b):
    print("getContours_1")
    box=b
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if (1500 < area):
            cv2.drawContours(imgContour_1,cnt,-1,(255,50,0),2)
            peri = cv2.arcLength(cnt,True)
            aprox = cv2.approxPolyDP(cnt,0.02*peri,False)
            objCor = len(aprox)
            x, y, w, h = cv2.boundingRect(aprox)
            if (3 < objCor < 8):
                box += 1
                objectType = "OB=%d a=%s"%(box,area)
            else : objectType = "NONE"
            cv2.rectangle(imgContour_1,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour_1,objectType,
                        (x+(w//2)-80,y+(h//2)+50),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),1)
    print("number of objects in line 1", box)
    return (imgContour_1,box)

def getContours_2(img,b):
    print("getContours_2")
    box=b
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if (1500 < area):
            cv2.drawContours(imgContour_2,cnt,-1,(255,50,0),2)
            peri = cv2.arcLength(cnt,True)
            aprox = cv2.approxPolyDP(cnt,0.02*peri,False)
            objCor = len(aprox)
            x, y, w, h = cv2.boundingRect(aprox)
            if (3 < objCor <  10):
                box += 1
                objectType = "OB=%d a=%s"%(box,area)
            else : objectType = "NONE"
            cv2.rectangle(imgContour_2,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour_2,objectType,
                        (x+(w//2)-80,y+(h//2)+50),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),1)
    print("number of objects in line 2", box)
    return (imgContour_2,box)

def getContours(img,b,s,zz):
    print("getContours")
    box=b
    idx = s
    img_1 = zz
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if (15000 < area): # < 20000):
            cv2.drawContours(imgContour,cnt,-1,(255,50,0),2)
            peri = cv2.arcLength(cnt,True)
            #print("peri:")
            #print(peri)
            aprox = cv2.approxPolyDP(cnt,0.02*peri,False)
            objCor = len(aprox)
            x, y, w, h = cv2.boundingRect(aprox)

            rect = cv2.minAreaRect(aprox)
            bbox = cv2.boxPoints(rect)
            bbox = np.int0(bbox)
            cv2.drawContours(img, [bbox], 0, (0, 0, 255), 8)

            #print("x=%d y=%d w=%d h=%d" %(x,y,w,h))
            if (3 < objCor <  15):
                box += 1;
                objectType = "lane=%d a=%s"%(box,area)
                #objectType = "w=%d h=%d a=%s" %(w,h,area)
            else : objectType = "NONE"

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,objectType,
                        (x+(w//2)-80,y+(h//2)+50),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),1)

            idx += 1
            new_img = img_1[y:y + h, x:x + w]
            #cv2.imshow("croped" + str(idx), new_img)
            cv2.imwrite(str(idx) + '.jpg', new_img)

            cv2.waitKey(15)

def capture_live_cam():
    print("fetch_live_cam")
    #cap = cv2.VideoCapture(0)
    for u in range(2):
        cap = cv2.VideoCapture(0)
        ret, imgt = cap.read()
    cv2.imwrite("Shapes.jpg", imgt)

def fetch_image():
    img = cv2.imread("Shapes.jpg", -1)
    imgContour = img.copy()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
    imgCanny = cv2.Canny(imgBlur, 50, 100)
    cv2.imshow("original", img)
    cv2.imshow("canny", imgCanny)
    return (imgCanny, imgContour, img)


#cap = capture_live_cam()
imgCanny,imgContour,img = fetch_image()
while y:
    print("While1")
    box = 0
    tri = 0
    getContours(imgCanny, box, idx, img)
    cv2.waitKey(15)

    boxb = 0
    image = cv2.imread("1.jpg", -1)
    imgContour_1 = image.copy()
    imgGray_1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imgBlur_1 = cv2.GaussianBlur(imgGray_1, (7, 7), 1)
    imgCanny_1 = cv2.Canny(imgBlur_1, 50, 100)
    imgContour_r,boxb = getContours_1(imgCanny_1,box)
    #cv2.imshow("canny_1", imgCanny_1)
    cv2.imshow("this_1", imgContour_r)

    boxa = 0
    image_a = cv2.imread("2.jpg", -1)
    imgContour_2 = image_a.copy()
    imgGray_2 = cv2.cvtColor(image_a, cv2.COLOR_BGR2GRAY)
    imgBlur_2 = cv2.GaussianBlur(imgGray_2, (7, 7), 1)
    imgCanny_2 = cv2.Canny(imgBlur_2, 50, 100)
    imgContour_ra,boxa = getContours_2(imgCanny_2, box)
    #cv2.imshow("canny_2", imgCanny_2)
    cv2.imshow("this_2", imgContour_ra)
    cv2.imshow("Con", imgContour)

    if(cv2.waitKey()):
        y = 0
        cv2.destroAllWindows()