import cv2
import numpy as np
objectfile ='resources/objects'
objectnames = []
width = 320 # we are using yolov3 320
confthreshold = 0.4
nmsthreshold = 0.3 # mininmum threshold
with open(objectfile,'r')as m:
    objectnames=m.read().rstrip('\n').split('\n')


model_configuration= 'resources/yolov3-tiny.cfg'
model_weight = 'resources/yolov3-tiny.weights'
net =cv2.dnn.readNetFromDarknet(model_configuration,model_weight)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
cap = cv2.VideoCapture(2)
def findobject (results ,vid):
    ht,wt ,ct = vid.shape
    bbox =  [] # contatin the value of ht and wt
    # if we have a good object detection we put it in these lists
    classIds =[]
    confs =[ ]
    for output in results:
        for det in output:
            scores = det[5:] # remove the first 5 elements from 85
            classId = np.argmax(scores) # get the index max value
            confidence = scores[classId] # get the max value which is the confidence
            # next filter the object
            if confidence > confthreshold : # if we have a good detection conf > 0.5
                # save the width and the height
                w,h =int (det[2]* wt ),int(det[3]*ht ) # pixel values
                x,y = int((det[0]*wt) -w/2) ,int( (det[1]*ht)-h/2)# get the center point coordination
                bbox.append([x,y,w,h])
                classIds.append(classId)
                confs.append(float(confidence) )
# there is an overlapping of boxes so we will pick the boxwith the most heighest confidence box and supress the others
# this function will tell us wich bbx to keep by giving theire indeces (pos)
    indices = cv2.dnn.NMSBoxes(bbox,confs,confthreshold,nmsthreshold)
    for i in indices :
        #i=i[0]
        box = bbox [i]
        x,y,w,h = box [0],box[1],box[2],box[3]
        # draw the boxes
        cv2.rectangle(vid,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.rectangle(vid, (x, (y+h) - 35), (x+w,y+h ), (0, 255, 0), cv2.FILLED)
        cv2.putText(vid,f'{objectnames[classIds[i]].upper()}{int(confs[i]*100)}%',(x+6,(y+h)-6),cv2.FONT_ITALIC,0.6,(0,0,0),2)



while True :
    success,vid =cap.read()# the network only accept a certain type of img called blob(binary large object )
    blob = cv2.dnn.blobFromImage(vid,1/255,(width,width),[0,0,0],1,crop=False)
    net.setInput(blob)
    # there are 3 outpu (layer )
    # first get the names of eeach layer
    layersnames =net.getLayerNames()
    #print (layername)
    # print the names of layers // i-1 cause  i starts counting from 1
    outputNames = [(layersnames[i-1]) for i in net.getUnconnectedOutLayers()]
    #print (outputNames)
    # finf outputs of 3 layers
    results = net.forward(outputNames) # type of results is list
    # print(results[0].shape)# (300,85)
    # print(results[1].shape) # (1200,85)
    # print(results[2].shape)# (4800,85)

# what is  (300, 85) (1200, 85)(4800, 85)
    # the first layer provides us 300 bouding boxes are the loction of images
    # same for the second and third layer
    # we have a totol 300+4800+1200 bouding boxes that contains x and y value  the height the width and object propability
    # see if the propability of an objetc is good enaugh or not (if it is good we put it in new list )
    # print(results[0][0])
    findobject(results,vid)


    cv2.imshow('vid',vid)
    if (cv2.waitKey(1) & 0xFF==ord('q')):
     break

cap.release()
