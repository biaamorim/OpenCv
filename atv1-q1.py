import cv2 as cv
import numpy as np

img = cv.imread('horaDeAventura.jpeg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#cores
blue=[(71 , 107 , 78),(117, 255, 211)]
red =[(0, 50, 50), (10, 255, 255)]
green=(50, 180,60)
green1=(130, 200,89)
yellow=(9, 220, 204)
yellow1=(110, 400, 250)


#azul
blue_mask = cv.inRange(hsv, np.array(blue[0]), np.array(blue[1]))
blue_contours = cv.findContours(blue_mask, cv.RETR_EXTERNAL, cv.FONT_HERSHEY_COMPLEX)[0]
blue_contours = sorted(blue_contours, key=cv.contourArea, reverse=True)[:2]


if blue_contours: 
    for contour in blue_contours:
        (cx, cy), radius = cv.minEnclosingCircle(contour)
        cv.putText(img, "Azul", (int(cx) + 50, int(cy)), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 2)
        cv.circle(img, (int(cx), int(cy)), int(radius), (194, 100, 78), 3)
        

#vermelho
red_mask = cv.inRange(hsv, np.array(red[0]), np.array(red[1]))
red_contours = cv.findContours(red_mask, cv.RETR_EXTERNAL, cv.FONT_HERSHEY_COMPLEX)[0]
red_contours = sorted(red_contours, key=cv.contourArea, reverse=True)[:4]

if red_contours:
    for contour in red_contours:
        (cx, cy), radius = cv.minEnclosingCircle(contour)
        cv.putText(img, "Vermelho", (int(cx), int(cy)), cv.FONT_HERSHEY_COMPLEX, 0.9, (50, 50, 255), 1)
        cv.circle(img, (int(cx), int(cy)), int(20),(50, 50, 255), 6)


#verde
green_mask = cv.inRange(hsv, green, green1)
green_contours = cv.findContours(green_mask, cv.RETR_EXTERNAL, cv.FONT_HERSHEY_COMPLEX)[0]
green_contours = sorted(green_contours, key=cv.contourArea, reverse=True)[:2]


if green_contours[:2]: 
    for contour in green_contours:
        (cx, cy), radius = cv.minEnclosingCircle(contour)
        cv.putText(img, "Verde", (int(cx), int(cy)), cv.FONT_HERSHEY_COMPLEX, 1, (60, 180,60), 2)
        cv.circle(img, (int(cx), int(cy)), int(20), (60, 180,60), 3)

#amarelo
yellow_mask = cv.inRange(hsv, yellow, yellow1)
yellow_contours = cv.findContours(yellow_mask, cv.RETR_EXTERNAL, cv.FONT_HERSHEY_COMPLEX)[0]
yellow_contours = sorted(yellow_contours, key=cv.contourArea, reverse=True)[:2]


if yellow_contours: 
    for contour in yellow_contours:
        (cx, cy), radius = cv.minEnclosingCircle(contour)
        cv.putText(img, "Amarelo", (int(cx), int(cy)), cv.FONT_HERSHEY_COMPLEX, 1, (5, 300, 24), 2)
        cv.circle(img, (int(cx), int(cy)), int(radius), (39,85,99), 3)

cv.imshow("Color Detected", img)
cv.waitKey(0)