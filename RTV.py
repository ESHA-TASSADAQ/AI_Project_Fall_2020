import argparse


#argument
aParse = argparse.ArgumentParser()
aParse.add_argument("-p","--prototxt",required=True,help="path to Caffe 'deploy' prototxt file")
aParse.add_argument("-m","--model",required=True,help="path to Cafee pre-trained model")
aParse.add_argument("-c","--confidence",type=float, default=0.2,help="minimum probability to filter weak detections")
aParse.add_argument("-v","--video_source",type=int,default=0,help="video source (default = 0, external usually = 1)")
args = vars(aParse.parse_args())

