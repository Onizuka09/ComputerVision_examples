import cv2
import face_recognition


#set the serial port

# step 1 :load the img test and get the encodings (measurments  ) 
img = face_recognition.load_image_file('resources/faces/moktar.jpg')
img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
encodings = face_recognition.face_encodings(img)
#step 2 : get the featurs from the webcam 
cap = cv2.VideoCapture(2)
while True :

 sucess, img=cap.read()
 # resize the img to reduce the time of processing 
 imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
 imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
 facesCurFrame = face_recognition.face_locations(imgS)
 encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
 # compare the encodings of the webcam to the encoding taken from the img 
 for  encodeFace, faceloc in zip(encodesCurFrame, facesCurFrame):
    results = face_recognition.compare_faces(encodings, encodeFace)
    facedist = face_recognition.face_distance(encodings, encodeFace)
    print(facedist)
    # draw a rectangle around the detected face 
    y1, x2, y2, x1 = faceloc
    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
    cv2.rectangle(img, (x1,y1),(x2,y2),(255,0,255),1)
    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
    cv2.putText(img,f'{results} {round(facedist[0],2)}', (x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
    
   
 cv2.imshow('Webcam',img)
 if cv2.waitKey(1) & 0xFF == ord('e'):
            break
cap.release()
