import numpy as np
import cv2
import keyboard
import time


def identifyColor(l):

    color = ''
    colorList = []
    for i in l:

        if i[1] < 45:
            color = 'W'
        elif i[0] < 4 or i[0] > 175:
            color = 'R'
        elif i[0] < 18:
            color = 'O'
        elif i[0] < 33:
            color = 'Y'
        elif i[0] < 85:
            color = 'G'
        elif i[0] < 131:
            color = 'B'

        colorList.append(color)

    print(colorList)
    return colorList


# program starts here
cap = cv2.VideoCapture(0)
allsides = []

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cx = int(width/2)
    cy = int(height/2)

    cv2.circle(frame, (cx-55, cy-65), 5, (255, 0, 0), 3)  # left upper
    cv2.circle(frame, (cx, cy-65), 5, (255, 0, 0), 3)  # central upper
    cv2.circle(frame, (cx+55, cy-65), 5, (255, 0, 0), 3)

    cv2.circle(frame, (cx-55, cy), 5, (255, 0, 0), 3)
    cv2.circle(frame, (cx, cy), 5, (255, 0, 0), 3)  # central
    cv2.circle(frame, (cx+55, cy), 5, (255, 0, 0), 3)

    cv2.circle(frame, (cx-55, cy+65), 5, (255, 0, 0), 3)
    cv2.circle(frame, (cx, cy+65), 5, (255, 0, 0), 3)  # central lower
    cv2.circle(frame, (cx+55, cy+65), 5, (255, 0, 0), 3)

    if keyboard.is_pressed('a'):
        time.sleep(0.5)
        c0 = hsv_frame[cy-65, cx-55]
        c1 = hsv_frame[cy-65, cx]
        c2 = hsv_frame[cy-65, cx+55]

        c3 = hsv_frame[cy, cx-55]
        c4 = hsv_frame[cy, cx]
        c5 = hsv_frame[cy, cx+55]

        c6 = hsv_frame[cy+65, cx-55]
        c7 = hsv_frame[cy+65, cx]
        c8 = hsv_frame[cy+65, cx+55]

        val_list = [c0, c1, c2, c3, c4, c5, c6, c7, c8]
        allsides.append(identifyColor(val_list))

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

check = input("c = correct\tw= wrong : ")
while check == 'w':
    fac = int(input("enter face number of wrong element:"))
    ele = int(input("enter position of wrong element:"))
    rep = input("Enter color to replace : ")
    allsides[fac][ele] = rep
    print('Updated Colors = ', allsides)
    check = input("c = correct\tw= wrong : ")


print("Displaying entire cube:")
for i in allsides:
    print(i)
