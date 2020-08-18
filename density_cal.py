"""Camera position

Capture the image
System shall be able to capture the image of the traffic and save as jpeg file
Density Calculation

a. System shall be able to do the partiation in the captured image
b. System shall be able to calculate the number of vehicles in perticular part.
17/08/2020"""

import cv2
import numpy as np
vehicle_count = 0


def fetch_image(camera_en=0,image_path='Sa.png'):
    if camera_en:
        for u in range(2):
            captured_image = cv2.VideoCapture(0)
            ret, snapshot = captured_image.read()
        cv2.imwrite(image_path, snapshot)

    original_image = cv2.imread(image_path, -1)
    contour_image = original_image.copy()
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    blur_image = cv2.GaussianBlur(gray_image, (7, 7), 1)
    canny_image = cv2.Canny(blur_image, 50, 100)
    cv2.imshow("canny", canny_image)
    cv2.imshow("original", contour_image)
    return canny_image, contour_image


def detect_lane(cannyimage, output_image):
    object_count = 0
    index_value = 0
    contours, hierarchy = cv2.findContours(cannyimage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        object_area = cv2.contourArea(cnt)
        if 8000 < object_area:
            cv2.drawContours(output_image, cnt, -1, (255, 50, 0), 2)
            perimeter = cv2.arcLength(cnt, True)
            approximate_sides = cv2.approxPolyDP(cnt, 0.02*perimeter, False)
            objects_sides = len(approximate_sides)
            x, y, w, h = cv2.boundingRect(approximate_sides)
            rectangle = cv2.minAreaRect(approximate_sides)
            plot_points = cv2.boxPoints(rectangle)
            points = np.int0(plot_points)
            cv2.drawContours(output_image, [points], 0, (0, 0, 255), 8)
            if 3 < objects_sides < 15:
                object_count += 1
                object_type = "lane=%d a=%s" % (object_count, object_area)
            else:
                object_type = "NONE"

            cv2.rectangle(output_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(output_image, object_type, (x+(w//2)-80, y+(h//2)+50), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 1)
            index_value += 1
            output_image = output_image[y:y + h, x:x + w]
            cv2.imshow("cropped" + str(index_value), output_image)
            cv2.imwrite(str(index_value) + 'cropped.png', output_image)


def getcontours(img,b,s,zz):
    print("getcontours")
    box=b
    idx = s
    img_1 = zz
    imgContour = zz
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if (1500 < area): # < 20000):
            cv2.drawContours(imgContour,cnt,-1,(255,50,0),2)
            peri = cv2.arcLength(cnt,True)
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
            cv2.putText(imgContour,objectType,(x+(w//2)-80,y+(h//2)+50),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),1)

            idx += 1
            new_img = img_1[y:y + h, x:x + w]
            #cv2.imshow("croped" + str(idx), new_img)
            cv2.imwrite(str(idx) + '.png', new_img)

            cv2.waitKey(15)





image_outline, image_raw= fetch_image()
detect_lane(cannyimage=image_outline, output_image=image_raw)

#getcontours(image_outline, 0, 0, image_raw)
cv2.waitKey()

