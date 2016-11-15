import cv2
import sys
import numpy as np
import time
def nothing(x):
    pass

cam = cv2.VideoCapture(0)
ret,img = cam.read()
cv2.namedWindow('tb')

# create trackbars for color change
#cv2.createTrackbar('HMin','tb',0,179,nothing) # Hue is from 0-179 for Opencv
#cv2.createTrackbar('HMax','tb',0,179,nothing)
#cv2.createTrackbar('SMin','tb',0,255,nothing)
#cv2.createTrackbar('SMax','tb',0,255,nothing)
#cv2.createTrackbar('VMin','tb',0,255,nothing)
#cv2.createTrackbar('VMax','tb',0,255,nothing)

# Set default value for MAX HSV trackbars.
#cv2.setTrackbarPos('HMax', 'tb', 179)
#cv2.setTrackbarPos('SMax', 'tb', 255)
#cv2.setTrackbarPos('VMax', 'tb', 255)

# Output Image to display
output = img
while(1):
      ret,img = cam.read()
      t1=time.time()
      # Create HSV Image and threshold into a range.
      hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
      # get current positions of all trackbars
      #hMin = cv2.getTrackbarPos('HMin','tb')
      #sMin = cv2.getTrackbarPos('SMin','tb')
      #vMin = cv2.getTrackbarPos('VMin','tb')

      #hMax = cv2.getTrackbarPos('HMax','tb')
      #sMax = cv2.getTrackbarPos('SMax','tb')
      #vMax = cv2.getTrackbarPos('VMax','tb')

      # Set minimum and max HSV values to display
      lower = np.array([20, 100, 100])
      upper = np.array([60, 255, 255])
      
      mask = cv2.inRange(hsv, lower, upper)
      output = cv2.bitwise_and(img,img, mask= mask)

      erodelement = np.ones((5,5),np.uint8)
      dilatelement = np.ones((8,8),np.uint8)

      erosion = cv2.erode(output,erodelement,iterations = 1)
      dilation = cv2.dilate(erosion,dilatelement,iterations = 1)

      dilation = cv2.inRange(dilation, lower, upper)
      #cv2.flip(dilation,1,dilation)

      countours,hierarchy=cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
      
      # Display output image
      cv2.imshow('image',output)
      #cv2.imshow('eroded image',erosion)
      for cnt in countours:
      #print(cnt)
            (x,y),radius = cv2.minEnclosingCircle(cnt)
            center = (int(x),int(y))
            radius = int(radius)
            #print(x)
            #print("  ")
            #print(y)
            #print("\n")
            cv2.drawContours(img,[cnt],0,(0,255,0),1)   # draw contours in green color
            cv2.circle(img,center,radius,(0,255,0),2)
            cv2.imshow('final image',img)
      print(time.time()-t1)
      # Wait for 33 milliseconds: 30FPS
      k = cv2.waitKey(33) & 0xFF
      if k == 27:
            break
cam.release()
cv2.destroyAllWindows()
