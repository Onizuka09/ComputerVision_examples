from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject
import serial
import time
import cv2


ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1)
data = SerialObject("/dev/ttyACM0")
cap = cv2.VideoCapture(2)
detector = FaceDetector()
xpose =0
ser_initX = 90
ser_initY = 90
prevX = ser_initX
height= 240            #360
width= 320             #640
set = False
xe =0

# cap.set(3, width)  # define the width (id number 3)
# cap.set(4, height)  # define the height (id number 4 )

def map( x,  in_min,  in_max,  out_min,  out_max):

  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


while True:

    success, img = cap.read()
    #get the center of the frame (which is the center of the camera)
    #print(img.shape)
    x0 = int(img.shape[1] /2)
    y0 = int(img.shape[0]/2)
    #print(x1, y1)
    # draw the center of the frame (the white box )
    x_rec = x0 - 20 # white rectangle coordinates
    y_rec = y0 - 20
    img= cv2.circle(img,(x0,y0),3,(0,255,0),cv2.FILLED)
    img = cv2.rectangle(img, (x_rec, y_rec), (x_rec + 40, y_rec + 40), (255, 255, 255), 1)
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


        # if ( xf <= x0+20 and xf >=x0-20  ):
        #     xe=0
        # else :
        #     xe = x0 - xf
        # #convert the error to servo position (90 -->0)
        # xse = int((xe/x0)*90)
        # #claculate the new servo position
        # xpose = prevX + xse
        # if (xpose >=180 ):
        #     xpose =180
        # if (xpose<=0):
        #     xpose=0
        # prevX=xpose
        # print(f"erro:{xse}::new servo position {xpose}")



        #print(f"x:{xf}::y:{yf}")
        xpose = int(map(xf, 0, img.shape[1], 180, 0))
        print(f"xf pose:{xf}")
        string = 'X{}'.format(xpose)

        #print(string)
        ser.write(string.encode('utf-8'))
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()