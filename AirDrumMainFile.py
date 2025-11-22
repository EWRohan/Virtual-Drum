import cv2
import imutils
import numpy as np
import pyautogui

def Press(key):
    pyautogui.keyDown(key)

vid = cv2.VideoCapture(0)
while True:
        _, frame = vid.read()
        frame = cv2.flip(frame,1)
        frame = imutils.resize(frame, height=200, width=400)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lowblue = np.array([22,100,100])
        highblue = np.array([75,255,255])

        blue_mask = cv2.inRange(hsv, lowblue, highblue)

        contours,hierachy=cv2.findContours(blue_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)

        for cnt in contours:
                (x,y,w,h) = cv2.boundingRect(cnt)
                cv2.circle(frame,(x+(w//2),y+(h//2)),(w//2),(0,255,0),2)
                if x > 60 and y > 24 and x < 130 and y < 94:
                        Press('9') #crash(top-left)
                        break
                if x > 165 and y > 24 and x < 235 and y < 94:
                        Press('w') #tom2(top-mid)
                        break
                if x > 270 and y > 24 and x < 340 and y < 94:
                        Press('7') #ride(top-right)
                        break

                if x > 20 and y > 125 and x < 90 and y < 195:
                        Press('5') #hithat(left1)
                        break
                if x > 20 and y > 215 and x < 90 and y < 285:
                        Press('2') #snare(left2)
                        break

                if x > 310 and y > 125 and x < 380 and y < 195:
                        Press('e') #tom3(right1)
                        break
                if x > 310 and y > 215 and x < 380 and y < 285:
                        Press('1') #kick(right2)
                        break



        
        
        cv2.circle(frame,(95,59),35,(255,0,0),2) #top left
        cv2.putText(frame, 'Crash', (71,65), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1,cv2.LINE_AA)

        
        cv2.circle(frame,(200,59),35,(255,0,0),2) # top 2nd
        cv2.putText(frame, 'Tom 2', (174,65), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1,cv2.LINE_AA)

        cv2.circle(frame,(305,59),35,(255,0,0),2) #top 3rd
        cv2.putText(frame, 'Ride', (288,65), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1,cv2.LINE_AA)

        cv2.circle(frame,(55,160),35,(255,0,0),2) #left
        cv2.putText(frame, 'Hit-Hat', (31,166), cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,255),1,cv2.LINE_AA)
        
        cv2.circle(frame,(55,250),35,(255,0,0),2) #left
        cv2.putText(frame, 'Snare', (33,256), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1,cv2.LINE_AA)
        
        cv2.circle(frame,(345,160),35,(255,0,0),2) #right
        cv2.putText(frame, 'Tom 3', (320,166), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1,cv2.LINE_AA)
        
        cv2.circle(frame,(345,250),35,(255,0,0),2) #right
        cv2.putText(frame, 'Kick', (329,256), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1,cv2.LINE_AA)
        

        
        cv2.imshow("Air-Drum", frame)
        key = cv2.waitKey(1)
        if key == 27:
                break

vid.release()
cv2.destroyAllWindows()
