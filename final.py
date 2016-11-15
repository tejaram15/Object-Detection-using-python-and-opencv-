from time import sleep
import serial
import cv2
import sys
import numpy as np

def nothing(x):
    pass

cam = cv2.VideoCapture(0)
ret,img = cam.read()
cv2.namedWindow('tb')

ser = serial.Serial('COM8', 9600) # Establish the connection on a specific port

output = img
while(1):
      ret,img = cam.read()
      # Create HSV Image and threshold into a range.
      hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
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
            ser.write(str(x))
            print ser.readline()
            sleep(.1)
            #print(x)
            #print("  ")
            #print(y)
            #print("\n")
            cv2.drawContours(img,[cnt],0,(0,255,0),1)   # draw contours in green color
            cv2.circle(img,center,radius,(0,255,0),2)
            cv2.imshow('final image',img)
      
      # Wait for 33 milliseconds: 30FPS
      k = cv2.waitKey(33) & 0xFF
      if k == 27:
            break
cam.release()
cv2.destroyAllWindows()
