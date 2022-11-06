import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Rect', rectangle)
cv.imshow('Circ', circle)

bitwise_and = cv.bitwise_and(rectangle, circle) #Returns intersecting sections
#cv.imshow('Bitwise AND', bitwise_and)

bitwise_or = cv.bitwise_or(rectangle, circle) #Returns intersecting and not intersecting sections
#cv.imshow('Bitwise OR', bitwise_or)

bitwise_xor = cv.bitwise_xor(rectangle, circle) #Returns non intersecting sections
cv.imshow('Bitwise XOR', bitwise_xor)

bitwise_not = cv.bitwise_not(rectangle) #Inverts colors basically
cv.imshow('Bitwise NOT', bitwise_not)

cv.waitKey(0)