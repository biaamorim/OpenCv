import cv2 as cv
import numpy as np

img = cv.imread('./horaDeAventura.jpeg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

blue=[(71 , 107 , 78),(117, 255, 211)]
red =[(0, 50, 50), (10, 255, 255)]
green=[(36,25,25),(86, 255,255)]
yellow=(58, 100, 84)
yellow1=(41, 100,45)

blue_mask = cv.inRange(hsv, np.array(blue[0]), np.array(blue[1]))
blue_contours = cv.findContours(blue_mask, cv.RETR_EXTERNAL, cv.FONT_HERSHEY_COMPLEX)[0]
blue_contours = sorted(blue_contours, key=cv.contourArea, reverse=True)[:2]


if blue_contours: 
    for contour in blue_contours:
        (cx, cy), radius = cv.minEnclosingCircle(contour)
        cv.putText(img, "Azul", (int(cx) + 50, int(cy)), cv.FONT_HERSHEY_COMPLEX, 1, (194, 100, 78), 2)
        cv.circle(img, (int(cx), int(cy)), int(radius), (194, 100, 78), 3)
        


red_mask = cv.inRange(hsv, np.array(red[0]), np.array(red[1]))
red_contours = cv.findContours(red_mask, cv.RETR_EXTERNAL, cv.FONT_HERSHEY_COMPLEX)[0]
red_contours = sorted(red_contours, key=cv.contourArea, reverse=True)[:2]

if red_contours:
    for contour in red_contours:
        (cx, cy), radius = cv.minEnclosingCircle(contour)
        cv.putText(img, "Vermelho", (int(cx), int(cy)), cv.FONT_HERSHEY_COMPLEX, 0.9, (360, 100, 100), 1)
        cv.circle(img, (int(cx), int(cy)), int(radius), (360, 100, 95), 6)



green_mask = cv.inRange(hsv, np.array(green[0]), np.array(green[1]))
green_contours = cv.findContours(green_mask, cv.RETR_EXTERNAL, cv.FONT_HERSHEY_COMPLEX)[0]
green_contours = sorted(green_contours, key=cv.contourArea, reverse=True)[:1]


if green_contours: 
    for contour in green_contours:
        (cx, cy), radius = cv.minEnclosingCircle(contour)
        cv.putText(img, "Verde", (int(cx), int(cy)), cv.FONT_HERSHEY_COMPLEX, 1, (86, 255,255), 2)
        cv.circle(img, (int(cx), int(cy)), int(radius), (86, 255,255), 3)

yellow_mask = cv.inRange(hsv, yellow, yellow1)
yellow_contours = cv.findContours(yellow_mask, cv.RETR_EXTERNAL, cv.FONT_HERSHEY_COMPLEX)[0]
yellow_contours = sorted(yellow_contours, key=cv.contourArea, reverse=True)[:3]


if yellow_contours: 
    for contour in yellow_contours:
        (cx, cy), radius = cv.minEnclosingCircle(contour)
        cv.putText(img, "Amarelo", (int(cx), int(cy)), cv.FONT_HERSHEY_COMPLEX, 1, (86, 255,255), 2)
        cv.circle(img, (int(cx), int(cy)), int(radius), (39,85,99), 3)
cv.imshow("Color Detected", img)
cv.waitKey(0)