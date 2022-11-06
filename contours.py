import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread('Picture/pointing.png')
#resized_image = rescaleFrame(img, 0.4)

blank = np.zeros(img.shape, dtype = 'uint8')
#cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT) #Method 1, blurring the image and then using canny to limit contours

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

#ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) #Method 2, using thresholding to limit contours
#cv.imshow('Threshold', thresh)

contours, heirarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,255,0), 2)
cv.imshow('Contours', blank)

cv.waitKey(0)