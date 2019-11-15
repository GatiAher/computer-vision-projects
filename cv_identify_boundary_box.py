

# cv_identify_boundary_box.py

""" GOAL: Given an image containing a rotated block of text 
at an unknown angle, we need to compute the text skew by 
computing a bounding box"""

""" RESOURCES:
https://www.pyimagesearch.com/2017/02/20/text-skew-correction-opencv-python/
"""

##########
# SET UP #
##########

# import the necessary packages
import numpy as np
import argparse
import cv2

#############
# GET IMAGE #
#############

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image file")
args = vars(ap.parse_args())
 
# load the image from disk
image = cv2.imread(args["image"])
cv2.imshow("Input", image)

# convert the image to grayscale and flip the foreground
# and background to ensure foreground is now "white" and
# the background is "black"
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray)

# threshold the image, setting all foreground pixels to
# 255 and all background pixels to 0
thresh = cv2.threshold(gray, 0, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imshow("Threshold", thresh)


cv2.waitKey(0)
