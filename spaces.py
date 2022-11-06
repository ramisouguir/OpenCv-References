import cv2 as cv

img = cv.imread('Picture/pointing.png')
cv.imshow('Image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#cv.imshow('RGB', rgb)

hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
#cv.imshow('HSV -> BGR', hsv_bgr)

cv.waitKey(0)