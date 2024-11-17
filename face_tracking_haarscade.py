import cv2
import math
# import the haascade file
faceCascade = cv2.CascadeClassifier('resources/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
max_target_distance= 40
center = []
while True:
    _, img = cap.read() # 0 default wbecam of the laptopq


    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# get the face location
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    #print(faces)

        #draw the rectangle
    if len(faces) >= 1:  # if face(s) detected
        faces = list(faces)[0]  # if several faces found use the first one

        x = faces[0]
        y = faces[1]
        w = faces[2]
        h = faces[3]

        center_face_X = int(x + w / 2)
        center_face_Y = int(y + h / 2)
        height, width, channels = img.shape

        distance_from_center_X = (center_face_X - width / 2)
        distance_from_center_Y = (center_face_Y - height / 2)

        target_distance = math.sqrt((distance_from_center_X ) ** 2 + (distance_from_center_Y ) ** 2)  # calculate distance between image center and face center

        cv2.rectangle(img, (center_face_X - 10, center_face_Y), (center_face_X + 10, center_face_Y),(255,0,0), 2) # draw first line of the cross

        cv2.rectangle(img ,(center_face_X, center_face_Y - 10), (center_face_X, center_face_Y + 10),(255,0,0), 2)# draw second line of the cross

        cv2.circle(img, (int(width / 2), int(height / 2)), int(max_target_distance), (0,255,0), 2)  # draw circle

    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
