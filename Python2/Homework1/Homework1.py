#%%
import cv2 as cv

#%%

#Problem1
img = cv.imread('practical_homework/pic1.jpg')
cv.imshow('pic1', img) 

img = cv.imread('practical_homework/pic2.jpg')
cv.imshow('pic2', img) 

img = cv.imread('practical_homework/pic3.jpg')
cv.imshow('pic3', img) 
cv.waitKey(0)

# %%

#Problem2
capture = cv.VideoCapture('practical_homework/vid1.mp4')
while True:
    isTrue, frame = capture.read() 
   
    if isTrue:
        cv.imshow('vid1', frame)
    else:
        print('empty frame')
        exit(1)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows() 
cv.waitKey(0)

# %%
#Problem3
def rescaleFrame(frame, scale = 0.75):
    
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('practical_homework/pic1.jpg')

img_rescaled = rescaleFrame(img, 0.5)

cv.imshow('pic1', img)
cv.imshow('pic1_rescaled', img_rescaled)

cv.waitKey(0)

# %%

#Problem4
capture = cv.VideoCapture('practical_homework/vid1.mp4')

while True:
    isTrue, frame = capture.read() #returns the frams and a boolean indicarting if it was successfully read
    
    if frame is not None: #or if isTrue
        frame_rescaled = rescaleFrame(frame, 0.5)
        cv.imshow('vid1', frame)
        cv.imshow('vid1_rescaled', frame_rescaled)
    else:
        print('empty frame')
        exit(1)
    
    #we don't want the video to display forever
    #when the letter 'd' is pressed, break out of the loop
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows() #distroying all windows since we don't need them anymore
    
cv.waitKey(0)
# %%

#Problem5
img = cv.imread('practical_homework/pic2.jpg')
img1 = cv.imread('practical_homework/pic2.jpg')
center = (int(img.shape[1]/2), int(img.shape[0]/2))
radius = int(img.shape[1]/10)
cv.circle(img,center,radius,(0, 0, 255),-1)

cv.imshow('Circled', img)
cv.imshow('pic2', img1)
cv.waitKey(0)
# %%

#Problem6

img = cv.imread('practical_homework/pic2.jpg')
img1 = cv.imread('practical_homework/pic2.jpg')
A = (int(img.shape[1]/2), int(img.shape[0]/2))
B = (A[0] + 100, A[1] + 50)
cv.rectangle(img,A ,B ,(67,130,255),2)

cv.imshow('Rectangle', img)
cv.imshow('pic2', img1)
cv.waitKey(0)
# %%

#Problem7

img = cv.imread('practical_homework/pic1.jpg')
img1 = cv.imread('practical_homework/pic1.jpg')
A = (img.shape[1],0)
B = (0,img.shape[0])
cv.line(img,A ,B, (255,0,0),2)

cv.imshow('Line', img)
cv.imshow('pic1', img1)
cv.waitKey(0)
# %%
