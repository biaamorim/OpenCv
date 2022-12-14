import numpy as np
import cv2

cap = cv2.VideoCapture("danca.mp4")

frame_width =int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_heigth = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc= cv2.VideoWriter_fourcc('X', 'Y', 'I', 'D')
out =cv2.VideoWriter("output.avi", fourcc, 5.0, (1280, 720))
ret, frame1= cap.read()
ret, frame2= cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1,frame2)
    color = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(color,(5,5),0)

    _,thresh =cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    
    dilated = cv2.dilate(thresh,None,iterations=3)

    contours,_ = cv2.findContours( dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 900:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(322,13,93),2)
        cv2.putText(frame1, ("Doguinho dancando com o menino"),(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
    

    img =cv2.resize(frame1,(1280,720))

    out.write(img)
    
    cv2.imshow("Video",frame1)
    frame1 =frame2
    ret , frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()

