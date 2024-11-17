import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from cvzone.SerialModule import SerialObject
import mediapipe as mp
import math
data = SerialObject("/dev/ttyACM0")

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    # Get image frame
    success, img = cap.read()
    # Find the hand and its landmarks
    hands, img = detector.findHands(img)  # with draw
    # hands = detector.findHands(img, draw=False)  # without draw

    if hands:
        # Hand 1

        lmList1 = hand1["lmList"]  # List of 21 Landmark points

        print(lmList1[4], lmList1[8])
        x1, y1 = lmList1[4][0], lmList1[4][1]
        x2, y2 = lmList1[8][0], lmList1[8][1]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2  # get the center line
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), 0, 3)
        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
        length = math.hypot(x2 - x1, y2 - y1)  # get the length
        # print(length)
        # hand range from 10 to 300
        # led volume from 0 to 255
        val = np.interp(length, [15, 230], [0, 255])
        valbar = np.interp(length, [15, 230], [400, 150])
        cv2.rectangle(img, (8, 150), (60, 400), (255, 0, 0), 3)
        cv2.rectangle(img, (8, int(valbar)), (60, 400), (255, 0, 0), cv2.FILLED)
        # print(int(val))
        # data.sendData([val])
    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()