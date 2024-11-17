import cv2
import numpy as np
import face_recognition
# step 1  ; load the images
img = face_recognition.load_image_file('resources/faces/elon and ms elon.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

imgtest =  face_recognition.load_image_file('resources/faces/elon.jpg')
imgtest = cv2.cvtColor(imgtest, cv2.COLOR_BGR2RGB)

# step2 : finding the encodings (caracteristic of a face)
# get the encoing of the image
faceloc = face_recognition.face_locations(img)[0]
encodeimg = face_recognition.face_encodings(img)[0]

# get the encodings for the test image

faceloctest = face_recognition.face_locations(imgtest)
encodtest = face_recognition.face_encodings(imgtest,faceloctest)
#cv2.rectangle(imgtest,(faceloctest[3],faceloctest[0]),(faceloctest[1],faceloctest[2]),
 #             (255,0,255),1)

# step3 compare between the two images

results = face_recognition.compare_faces([encodeimg],encodtest)
facedist =  face_recognition.face_distance([encodeimg],encodtest)
print (results)
cv2.rectangle(img, (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]),(255,0,255),1)
cv2.putText(img,f'{results} {round(facedist[0],2)}', (50, 50),cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)


cv2.imshow('img2',img)
cv2.waitKey(0)


