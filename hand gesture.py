import cv2
from cvzone.HandTrackingModule import HandDetector
#import mediapipe as mp
cap = cv2.VideoCapture(0)
hcam = 480
wcam = 620
cap.set(3,wcam)
cap.set(4,hcam)


detect = HandDetector(detectionCon=0.8, maxHands=1)




while True:
    success,img= cap.read()

    hands, img = detect.findHands(img)  # with draw
    print(type(hands))
    if hands:
        hand1 =hands[0]
        #hand2=hands[1]
        # lmList1 = hand1["lmList"]  # List of 21 Landmark points
        # bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        # centerPoint1 = hand1['center']  # center of the hand cx,cy
        # handType1 = hand1["type"]  # Handtype Left or Right

        fingers1 = detect.fingersUp(hand1)

        # fingers2 = detect.fingersUp(hand2)
        print(fingers1)
        # print("\t")
        # print(fingers2)

        # if len(hands) == 2:
        #     # Hand 2
        #     hand2 = hands[1]
        #     lmList2 = hand2["lmList"]  # List of 21 Landmark points
        #     bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
        #     centerPoint2 = hand2['center']  # center of the hand cx,cy
        #     handType2 = hand2["type"]  # Hand Type "Left" or "Right"
        #
        #     fingers2 = detect.fingersUp(hand2)





    cv2.imshow('img',img )
    if cv2.waitKey(1) & 0xFF == ord('q') :
                break
cap.release()