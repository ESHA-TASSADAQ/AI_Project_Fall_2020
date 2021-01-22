import argparse
import numpy as np
import random
import imutils
from imutils.video import VideoStream,FPS
import time
import cv2


#argument
aParse = argparse.ArgumentParser()
aParse.add_argument("-p","--prototxt",required=True,help="path to Caffe 'deploy' prototxt file")
aParse.add_argument("-m","--model",required=True,help="path to Cafee pre-trained model")
aParse.add_argument("-c","--confidence",type=float, default=0.2,help="minimum probability to filter weak detections")
aParse.add_argument("-v","--video_source",type=int,default=0,help="video source (default = 0, external usually = 1)")
args = vars(aParse.parse_args())


#initialize class 
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]

#generatin colored boundry 
COLORS = np.random.uniform(0,255,size=(len(CLASSES),3))


print("Loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"],args["model"])
#net = cv2.dnn.readNetFromTensorflow(args["model"]) #incase for tensorflow model
#Initilze Video stream for camera
print("Starting Video Stream...")
#opening camera
vs = VideoStream(src=args["video_source"]).start()

time.sleep(1.0)
fps = FPS().start()

#To loop over the frames for the video stream
while True:
    #Resize of the sream
    frame = vs.read()
    frame = imutils.resize(frame,width = 550)

    #Using blob(datatype), it basically stores binary data, so like images can be saved too
    (h,w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame,(300,300)),0.007843, (300, 300), 127.5) #grabbing frame and converting it into blob

    #passing the blob through the network
    net.setInput(blob)
    detections = net.forward()

    #detection loop
    for i in np.arange(0,detections.shape[2]):
        confidence = detections[0,0,i,2]  #probability = confidence

        #making sure that the detection confidednce is greater than min
        if confidence > args["confidence"]:
            #creating boundary of the box
            idx = int(detections[0,0,i,1])
            box = detections[0,0,i,3:7] * np.array([w,h,w,h])
            (startX,startY,endX,endY) = box.astype("int")

            #BOx drawing
            label = "{}: {:.2f}%".format(CLASSES[idx],confidence * 100)
            cv2.rectangle(frame, (startX,startY),(endX,endY),COLORS[idx],2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(frame,label,(startX,y),cv2.FONT_HERSHEY_COMPLEX,0.5,COLORS[idx],2)

    #Output 
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1) & 0xFF

    #break from q
    if key == ord("q"):
        breakpoint

    fps.update()

fps.stop()
print("elapsed time: {:.2f}".format(fps.elapsed()))
print("approx. FPS: {:.2f}".format(fps.fps()))  

cv2.destroyAllWindows()
vs.stop()