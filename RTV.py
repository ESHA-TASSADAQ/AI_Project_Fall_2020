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
	"sofa", "train", "tvmonitor","Phone"]

#generatin colored boundry 
COLORS = np.random.uniform(0,255,size=(len(CLASSES),3))

#Initilze Video stream for camera
print("Starting Video Stream...")
#opening camera
vs = VideoStream(src=args["Video_source"]).start()

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





