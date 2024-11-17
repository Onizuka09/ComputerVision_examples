import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.SerialModule import SerialObject
#import mediapipe as mp
cap = cv2.VideoCapture(0)
hcam = 480
wcam = 620
cap.set(3,wcam)
cap.set(4,hcam)


detect = HandDetector(detectionCon=0.8, maxHands=2)
data = SerialObject("/dev/ttyACM0")



while True:
    success,img= cap.read()

    hands, img = detect.findHands(img)  # with draw

    if hands:
        hand1 =hands[0]
        fingers1 = detect.fingersUp(hand1)
        num= sum(fingers1)
        #print(num)

        if len(hands) == 2:
            # Hand 2
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmark points
            bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
            centerPoint2 = hand2['center']  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type "Left" or "Right"

            fingers2 = detect.fingersUp(hand2)
            num2=sum(fingers2)
            print(f'{num}+{num2}={num+num2}')
            data.sendData([num,num2])




    cv2.imshow('img',img )
    if cv2.waitKey(1) & 0xFF == ord('q') :
                break
cap.release()