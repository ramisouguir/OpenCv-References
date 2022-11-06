import cv2 as cv
import numpy as np

img = cv.imread('Picture/pointing.png')
cv.imshow('Image', img)

kernel = np.ones((2,2), np.uint8)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Gray', gray)

bilateral = cv.bilateralFilter(gray, 10, 35, 25)

cv.imshow('Bilateral', bilateral)

canny = cv.Canny(bilateral, 125, 175)

cv.imshow('Canny', canny)

dilated = cv.dilate(canny, kernel, iterations=1)

cv.imshow('Dilated', dilated)

dst = cv.cornerHarris(dilated,2,3,0.08)

dst = cv.dilate(dst, None)

img[dst>0.01*dst.max()]=[0,0,255]

cv.imshow('dst',img)

cv.waitKey(0)