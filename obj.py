import cv2
import numpy as np
# Callback Function for Trackbar (but do not any work)
def nothing(*arg):
    pass


#H_MIN=0
#H_MAX=255
#S_MIN=0
#S_MAX=255
#V_MIN=0
#V_MAX=255

WindowName = "Test"
TrackbarName1 = "H"
TrackbarName2 = "s"
TrackbarName3 = "V"
#TrackbarName4 = "S_MAX"
#TrackbarName5 = "V_MIN"
#TrackbarName6 = "V_MAX"

cv2.namedWindow(WindowName)

cv2.createTrackbar(TrackbarName1, WindowName, 0, 255, nothing)
cv2.createTrackbar(TrackbarName2, WindowName, 0, 255, nothing)
cv2.createTrackbar(TrackbarName3, WindowName, 0, 255, nothing)
#cv2.createTrackbar(TrackbarName4, WindowName, S_MAX, S_MIN, nothing)
#cv2.createTrackbar(TrackbarName5, WindowName, V_MIN, V_MAX, nothing)
#cv2.createTrackbar(TrackbarName6, WindowName, V_MAX, V_MIN, nothing)

cam = cv2.VideoCapture(0)
ret,img = cam.read()

Threshold = np.zeros(img.shape, np.uint8)

while True:
      ret,img = cam.read()
      cv2.imshow('op',img)
      #conversion to HSV color Space
      hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
      cp=hsv
      
      h=cv2.getTrackbarPos(TrackbarName1, WindowName)
      s=cv2.getTrackbarPos(TrackbarName2, WindowName)
      v=cv2.getTrackbarPos(TrackbarName3, WindowName)

      cp[:]=[h,s,v]
      
      cv2.imshow('op1', cp)
      cv2.imshow('op2', hsv)
      
      key=cv2.waitKey(10)
      if key==27:
            break
cam.release()
cv2.destroyAllWindows()
