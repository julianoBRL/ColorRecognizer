
# Python programs to find
# unique HSV code for color
# Importing the libraries openCV & numpy
import cv2
import numpy as np

def RGBtoHSV(red,green,blue):
  color = np.uint8([[[blue, green, red]]])
  hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
  return hsv_color

def RGBtoHSV2(red,green,blue):
  hsv_color = RGBtoHSV(red,green,blue)
  return hsv_color[0][0][0]