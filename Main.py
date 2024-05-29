
# Python program to identify
#color in images
# Importing the libraries OpenCV and numpy

import cv2
import numpy as np

from HSVGenerator import RGBtoHSV2

# Read the images
#img = cv2.imread("Resources/shapes.jpg")
image = cv2.imread("Resources/img1.jpeg")

# Resizing the image
#image = cv2.resize(img, (700, 600))

# Convert Image to Image HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Generate HSV from RGB value
HSV = RGBtoHSV2(255,0,0)

# Defining lower and upper bound HSV values
lower = np.array([HSV-10, 100, 100])
upper = np.array([HSV+10, 255, 255])

# Defining mask for detecting color
mask = cv2.inRange(hsv, lower, upper)
res = cv2.bitwise_and(image,image,mask = mask)

# Display Image and Mask
cv2.imshow("Image", image)
cv2.imshow("Mask", mask)
cv2.imshow("Mask+Image", res)

# Make python sleep for unlimited time
cv2.waitKey(0)