import cv2 as cv

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread('Picture/bella.jpg')
resized_image = rescaleFrame(img, 0.4)
cv.imshow('Color', resized_image)

gray = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

blur = cv.GaussianBlur(resized_image, (3,3), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

canny = cv.Canny(blur, 110,155)
canny2 = cv.Canny(resized_image, 125,175)
#cv.imshow('Canny', canny)
#cv.imshow('Canny2', canny2)

# dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)

# eroded = cv.erode(dilated, (7,7), iterations=3)
# cv.imshow('Eroded', eroded)

resize = cv.resize(resized_image, (500,500)) #to increase size of the image, change interpolation to cubic (better quality) or linear
cv.imshow('Resize', resize)

cropped = resized_image[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)