import cv2 as cv

img = cv.imread('Picture/pointing.png')
cv.imshow('Image', img)

#Averaging
average = cv.blur(img, (7,7))
#cv.imshow('Average Blur', average)

gauss = cv.GaussianBlur(img, (7,7), 0)
#cv.imshow('Gaussian Blur', gauss)

median = cv.medianBlur(img, 3) #Reduces more noise in the image
#cv.imshow('Median Blur', median)

bilateral = cv.bilateralFilter(img, 10, 35, 25) #Most used blur method because it keeps the edges clean
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)