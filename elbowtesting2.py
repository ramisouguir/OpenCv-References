import cv2 as cv
import numpy as np

img = cv.imread('Picture/pointing.png')
cv.imshow('Image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gauss = cv.GaussianBlur(gray, (9,9), 0)

canny = cv.Canny(gauss, 125, 175)
cv.imshow('Canny', canny)

corners = cv.goodFeaturesToTrack(canny,50,0.01,10)
corners = np.int0(corners)
for i in corners:
    x,y = i.ravel()
    cv.circle(img,(x,y),3,255,-1)

cv.imshow('Img', img)

cv.waitKey(0)