#%%
import cv2 as cv
import numpy as np
# %%

#Problem1
img = cv.imread('practical_homework/pic1.jpg')
cv.imshow('pic1', img) 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Gray', gray)

cv.waitKey(0)

# %%

#Problem2
img = cv.imread('practical_homework/pic1.jpg')
cv.imshow('pic1', img) 

blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

blur = cv.GaussianBlur(img, (11, 11), cv.BORDER_DEFAULT)
cv.imshow('Blur2', blur)

cv.waitKey(0)
# %%

#Problem3
img = cv.imread('practical_homework/pic2.jpg')
cv.imshow('pic2', img) 

canny = cv.Canny(img, 75, 125)
cv.imshow('Edges', canny)

blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 75,125)
cv.imshow('Blur edges', canny)

cv.waitKey(0)
# %%

#Problem4
img = cv.imread('practical_homework/pic2.jpg')
cv.imshow('pic2', img) 

width = img.shape[1]
height = img.shape[0]

resize = cv.resize(img, (width * 2, height), interpolation = cv.INTER_AREA) 
cv.imshow('Resize1', resize)

resize = cv.resize(img, (width, height//2), interpolation = cv.INTER_CUBIC) 
cv.imshow('Resize2', resize)

cv.waitKey(0)
# %%

#Problem5


def translate(img, x, y): 
    
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    
    return cv.warpAffine(img, transMat, dimensions)

def rotate(img, angle, rotPoint = None):
    
    (height, width) = (img.shape[0], img.shape[1])
    
    if rotPoint == None:
        rotPoint = (width//2, height//2)
        
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimensions)

img = cv.imread('practical_homework/pic2.jpg')
cv.imshow('pic2', img) 

translated = translate(img, 50, 100) #changed 200 to 100 to see result
cv.imshow('Translated', translated)

rotated = rotate(translated,50)
cv.imshow('Rotated', rotated)

flip = cv.flip(rotated, -1)
cv.imshow('Flip', flip)
cv.waitKey(0)
# %%

#Problem6

img = cv.imread('practical_homework/pic3.jpg')
cv.imshow('pic3', img) 

canny = cv.Canny(img, 75, 125)
contours = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)[0]

blank = np.zeros(img.shape, dtype = 'uint8')
cv.drawContours(blank, contours, -1, (255, 0, 20), 1) 
cv.imshow('Contours', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 75, 125)

contours = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)[0]
blank = np.zeros(img.shape, dtype = 'uint8')
cv.drawContours(blank, contours, -1, (100, 0, 98), 1) 
cv.imshow('Contours blur', blank)

cv.waitKey(0)

