import numpy as np
import face_recognition
import os # interact with the os
import cv2



path = 'resources/faces'
images = []
classNames = []

myList = os.listdir(path) # read the path of the images 
print(myList)
# load the path into a list images 
for im in myList:
     curImg = cv2.imread(f'{path}/{im}')# im is the name of oour image : a counter
     images.append(curImg) # add the curImg to imges list
     classNames.append(os.path.splitext(im)[0])
#print (classNames)
# print the test images
# for img ,names in zip(images ,classNames):
#      cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#      cv2.imshow(f'{names}',img)

# cv2.waitKey(0)

# get the encodins from the test images
def find_encodings(images):
    encodelist = []
    for img in images:
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode_test = face_recognition.face_encodings(img)[0]
        encodelist.append(encode_test)
    return encodelist

encodeListKnown = find_encodings(images)
print ('encoding complete')

# compare the images to the webcam

cap = cv2.VideoCapture(0)
while True:
    success,vid = cap.read() # cpa.read function resturns data and boolean
    imgS= cv2.resize(vid,(0,0),None,0.25,0.25) # 0,0 => no need to define any pixel size
    imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        results = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        #print(faceDis)
        results_Index = np.argmin(faceDis)
        if(results[results_Index]):
            name= classNames[results_Index]
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(vid, (x1, y1), (x2, y2), (255, 0, 255), 1)
            cv2.rectangle(vid, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(vid, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        else :
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(vid, (x1, y1), (x2, y2), (255, 0, 255), 1)
            cv2.rectangle(vid, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(vid,'unknown', (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)



    cv2.imshow('Webcam',vid)
    if cv2.waitKey(1) & 0xFF == ord('e'):
            break
cap.release()
