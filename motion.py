import cv2, time, pandas
from datetime import datetime

#Declaration
first_frame=None
status_list=[None,None]
times=[]

df=pandas.DataFrame(columns=["Start","End"]) #DataFrame to store the time values during which object dectection and movement appears 

video=cv2.VideoCapture(0)  #Create a VideoCapture object to record video using web cam (0 is to specify to use built-in camera)

while True:
    check, frame = video.read()
    status=0 #Status at the beginning of the recording is zero as the object is not visible

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #Convert the frame color to gray scale
    gray=cv2.GaussianBlur(gray,(21,21),0) #Convert the gray scale frame to Gaussian Blur

    if first_frame is None: #This will store the first image/frame of the video as video is nothing but multiple pictures shown in a sequence
        first_frame=gray 
        continue

    delta_frame=cv2.absdiff(first_frame,gray) #Calculates the difference between the first frame and the other frames
    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1] #Provides a threshold value, such that it will convert the difference value with less than 30 to black. If the difference is greater than 30 it will convert those pixels to white
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2) 
    (cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #Defines the contour area. Basically add the borders
