import cv2

# import the haascade file 
faceCascade = cv2.CascadeClassifier('resources/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read() # 0 default wbecam of the laptopq


    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# get the face location 
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    #print(faces)
    # draw the rectangle 
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        center = (    (int((w/2)+x)), (int((h/2)+y)))

        cv2.circle(img,center,1,(255,0,0),10)
        #print ("x = "+(str((w/2)+x))+" y="+ (str((h/2)+y)) )

    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
