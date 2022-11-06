import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread('Picture/bella.jpg')
resized_image = rescaleFrame(img, 0.4)
img = resized_image

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) #If the threshold value is above 150, color goes to white, if it's below, color goes to black. Thresh is the thresholded image that is returned from the function
#cv.imshow('Thresholded', thresh)

threshold_inv, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV) 
#cv.imshow('Thresholded Inverse', thresh_inv)

#Adaptive Thresholding
adaptive_thresh_m = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive Thresholding Mean", adaptive_thresh_m)

adaptive_thresh_g = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive Thresholding Gaussian", adaptive_thresh_g)

cv.waitKey(0)