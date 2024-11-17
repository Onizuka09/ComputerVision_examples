from cvzone.FaceDetectionModule import FaceDetector

import serial
import time
import cv2

ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1)

cap = cv2.VideoCapture(2)
detector = FaceDetector()
xpose =0
cmd_servo =320
# prev_cmd = 0
xe =0

# cap.set(3, width)  # define the width (id number 3)
# cap.set(4, height)  # define the height (id number 4 )

# def map( x):
#
#   return (x *(-0.051) +107)


while True:

    success, img = cap.read()
    #get the center of the frame (which is the center of the camera)
    #print(img.shape)
    x0 = int(img.shape[1] /2)
    y0 = int(img.shape[0]/2)
    #print(x1, y1)
    # draw the center of the frame (the white box )
    img= cv2.circle(img,(x0,y0),3,(0,255,0),cv2.FILLED)
    img = cv2.rectangle(img, (x0 - 20, y0 - 20), (x0 + 20, y0 + 20), (255, 255, 255), 1)
    #detect the face
    img, bboxs = detector.findFaces(img)
    #if the img is detected
    if bboxs:
        center = bboxs[0]["center"] # get the center of bbx
        x,y,w,h= bboxs[0]["bbox"] # get th coordinates of the bbx
        cv2.circle(img, (x0,y0), 3, (0, 255, 0), cv2.FILLED)
        # draw the center of the bbx
        cv2.circle(img, (center), 3, (0, 255, 0), cv2.FILLED)
        #draw a line between the center of the bbx and the center of the frame
        img = cv2.line(img, (x0, y0), center, (0, 255, 0), 1)
        xf = center[0]
        yf = center[1]
        #calculate the error

            # xe = xf - x0
            #     # claculate the new servo position
            # # prev_cmd =cmd_servo
            # #if (prev_cmd != cmd):
            # cmd_servo = cmd_servo + xe
            # cmd_servo = max (cmd_servo, 0  )
            # cmd_servo = min (cmd_servo,img.shape[1])
            # # # convet the servo position
            # xpose = int(map(cmd_servo))
        print(f"XFpos: {xf}::erro: {xe}::new servo position {cmd_servo}::: serv pos{xpose}")
            # # # send the servo position
        string = 'X{}'.format(xf)
            # print(string)
        ser.write(string.encode('utf-8'))



    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()