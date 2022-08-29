from ctypes import resize
import cv2 as cv

img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    # Works for images,videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# resizedImage = rescaleFrame(img)
# cv.imshow('Image', resizedImage)

def changeRes(width, height):
    # works only for live video
    capture.set(3,width)
    capture.set(4,height)


#Reading Videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame,scale=.20)

    cv.imshow('VIDEO',frame)
    cv.imshow('Video resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

# cv.waitKey(0)