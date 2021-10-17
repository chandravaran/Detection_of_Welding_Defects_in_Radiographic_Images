# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:15:10 2020

@author: Chandravaran K V
"""
# import the necessary packages
#This is what is explained in  Future Work 
import numpy as np
import imutils
import cv2
def test_countur(c):
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.2 * peri, True)
    # the contour is 'bad' if it is too small or too big
    if peri>160 or peri<1000:
        return 1
    else:
        return 0
image = cv2.imread("F:\\IP_mini_project\\split_images\\001_DGAFB1 (2)_2.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 77, 130) #finding edges 
cv2.imshow("Original", image)
counts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) #simple contour function
counts = imutils.grab_contours(counts)
mask = np.ones(image.shape[:2], dtype="uint8") * 255
#we create mask here
for i in counts:
	if test_countur(i):
		cv2.drawContours(mask, [i], -1, 0, -1)
# We are adding anding the mask to remove the Letters this 
# Have not added the part which recontructs the image so that it look uniform 
image = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask", mask)
cv2.imshow("After", image)
cv2.waitKey(0)
