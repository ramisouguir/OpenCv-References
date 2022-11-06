import cv2 as cv
import numpy as np

img = cv.imread('Picture/pointing.png')
cv.imshow('Image', img)

blank  = np.zeros(img.shape[:2], dtype='uint8') #Mask needs to be the exact same dimensions as the image being masked

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (30,30), (400,400), 255, -1)

mask = cv.bitwise_and(circle, rectangle)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked', masked)

cv.waitKey(0)