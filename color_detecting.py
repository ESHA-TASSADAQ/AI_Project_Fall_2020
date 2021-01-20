import cv2
import numpy as np
import pandas as pd
import argparse

#Reading the image with opencv
img = cv2.imread('colorpic.jpg')

#declaring global variables (are used later on)
clicked = False
r = g = b = xpos = ypos = 0

#Reading csv file with pandas and giving names to each column
index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

