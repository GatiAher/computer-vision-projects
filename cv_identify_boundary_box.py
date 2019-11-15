

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

###################
# TRANSFORM IMAGE #
###################

# convert the image to grayscale and flip the foreground
# and background to ensure foreground is now "white" and
# the background is "black"
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray)

# threshold the image, setting all foreground pixels to
# 255 and all background pixels to 0
thresh = cv2.threshold(gray, 0, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

#################################
# COMPUTE AND DRAW BOUNDARY BOX #
#################################

# grab the (x, y) coordinates of all pixel values that
# are greater than zero, then use these coordinates to
# compute a rotated bounding box that contains all
# coordinates
coords = np.column_stack(np.where(thresh > 0))
rect = cv2.minAreaRect(coords)
print("BOUNDING BOX", rect)

# DRAW BOUNDING BOW
box = cv2.boxPoints(rect)
box = np.int0(box)
# for some reason all the values are (y, x)
for i in range(len(box)):
	temp = box[i][0]
	box[i][0] = box[i][1]
	box[i][1] = temp
cv2.drawContours(image,[box],0,(0,0,255),2)

#########################################
# GET THE ANGLE BOUNDARY BOX IS ROTATED #
#########################################

angle = rect[-1]

# the `cv2.minAreaRect` function returns values in the
# range [-90, 0); as the rectangle rotates clockwise the
# returned angle trends to 0 -- in this special case we
# need to add 90 degrees to the angle
if angle < -45:
	angle = -(90 + angle)

# otherwise, just take the inverse of the angle to make
# it positive
else:
	angle = -angle

#############################
# ROTATE IMAGE TO DESKEW IT #
#############################

# rotate the image to deskew it
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(image, M, (w, h),
	flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

####################################
# PUT CORRECTION ANGLE IN RED TEXT #
####################################

## draw the correction angle on the image so we can validate it
cv2.putText(rotated, "Angle: {:.2f} degrees".format(angle),
	(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
 
################################
# SHOW INPUT AND ROTATED IMAGE #
################################

print("[INFO] angle: {:.3f}".format(angle))
cv2.imshow("Input", image)
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)