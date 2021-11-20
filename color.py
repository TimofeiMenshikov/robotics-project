import cv2 as cv
import numpy as np
def nothing (x):
	pass
img_bgr =  cv.imread('field.png')
cv.imshow('img',img_bgr)  
img = cv.cvtColor(img_bgr, cv.COLOR_BGR2LAB)
cv.namedWindow('image')
# create trackbars for color change
cv.createTrackbar('lowerL','image',0,255,nothing)
cv.createTrackbar('lowerA','image',0,255,nothing)
cv.createTrackbar('lowerB','image',0,255,nothing)
cv.createTrackbar('upperL','image',0,255,nothing)
cv.createTrackbar('upperA','image',0,255,nothing)
cv.createTrackbar('upperB','image',0,255,nothing)
# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'image',0,1,nothing)
while(1):
    
	k = cv.waitKey(1) & 0xFF
	if k == 27:
		break
    # get current positions of four trackbars
	lL = cv.getTrackbarPos('lowerL','image')
	lA = cv.getTrackbarPos('lowerA','image')
	lB = cv.getTrackbarPos('lowerB','image')
	uL = cv.getTrackbarPos ('upperL','image')
	uA = cv.getTrackbarPos ('upperA','image')
	uB = cv.getTrackbarPos ('upperB','image')
	s = cv.getTrackbarPos(switch,'image')
	
	lower = (lL,lA,lB)
	upper = (uL,uA,uB)
	if s == 0:
		cv.imshow('image',img_bgr)
	else:
		mask = cv.inRange(img, lower, upper)
		result = cv.bitwise_and(img_bgr, img_bgr, mask = mask)
		#cv.imshow('image',mask)
		cv.imshow('image',mask)
cv.destroyAllWindows()
