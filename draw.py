import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness = -1)

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1) #(image, positionx, positiony, radius, color)

cv.line(blank, (100,300), (200, 400), (255,255,255), thickness=3)

cv.putText(blank, 'Hello', (350,255), cv.FONT_HERSHEY_COMPLEX, 1.0, (100, 100, 40), 2)
cv.imshow('Draw', blank)

cv.waitKey(0)