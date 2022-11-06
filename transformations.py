import cv2 as cv
import numpy as np
from numpy.core.fromnumeric import resize

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread('Picture/bella.jpg')
resized_image = rescaleFrame(img, 0.4)
cv.imshow('Color', resized_image)

def translate(image, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (image.shape[1], image.shape[0])
    return cv.warpAffine(image, transMat, dimensions)

translated = translate(resized_image, 100, 100)
#cv.imshow('Translated', translated)

def rotate(image, angle, rotPoint = None):
    (height, width) = image.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(image, rotMat, dimensions)

rotated = rotate(resized_image, 45)
#cv.imshow('Rotated', rotated)

flipped = cv.flip(resized_image, 1) #1 for horizontal and 0 for vertical -1 for horizontal and vertical
#cv.imshow('Flipped', flipped)

cropped = resized_image[200:400, 300:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)