import cv2 
import os
import time
cap = cv2.VideoCapture(0)
startingT=0
prevT=0
fps=0
dir_name="captured_imges"
path ="/home/moktar"

while 1:
    isDirExist = os.path.exists(os.path.join(path,dir_name))
    _,img = cap.read()
    startingT = time.time()
    fps=1/(startingT-prevT)
    prevT = time.time()
    print(fps)
    cv2.putText(img, f"frame:{int(fps)}", (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 150), 1)
    cv2.imshow("vid", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

                
cv2.destroyAllWindows()