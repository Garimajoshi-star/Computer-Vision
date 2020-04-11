#To begin with image processing in Python or Anaconda environment, install the OpenCV library shown as:
pip create –name opencv-env python = 3.7.4
#Now, the OpenCV library will be activated using the following command:
pip activate opencv – env
#Let’s consider the following steps to read, write and display the input image using OpenCV:


# Import library
import cv2
# Read input image
image = cv2.imread('image_flower.jpg')# here enter the path of the file where it is stored.
#Resize the input image
scale_percent = 40
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
# Program 4: Display image
cv2.imshow('image_flower',resized) #the cv2.imshow function will display the resized image. 

# Write input file
cv2.imwrite('image_flower.png', resized)# cv2.imwrite() is being called for writing a file.
# Now, consider the following steps to perform colour conversion and edge detection in an input image:
# Import library
import cv2
import numpy as np
# Read input file
image = cv2.imread('Koala.jpg')
# Program 3: Resize and display the input image
scale_percent = 50
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow('Koala',resized)

# Convert input image colour
resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray_Koala',resized)

# Program 5: Edge detection
cv2.imwrite('edges_Koala.jpg',cv2.Canny(resized,200,300))
cv2.imshow('edges_Koala', cv2.imread('edges_Koala.jpg'))



# Program 1: Import libraries
import cv2 
import numpy as np
# Program 2: Read input file
vc = cv2.VideoCapture('Wildlife.wmv')
# Program 3: Display video file
if (vc.isOpened()== False):  
  print("Video file cannot be opened.")
# Run video file
while(vc.isOpened()):     
  ret, slide = vc.read() 
  if ret == True: 
    gray = cv2.cvtColor(slide, cv2.COLOR_BGR2GRAY)
    b = cv2.resize(slide,(320,120),fx=0,fy=0)
    cv2.imshow('Slide', gray)
# The video will keep on playing until the while condition remains true or all the video frames are displayed. Using cvtColor(), the RGB video will be converted into BGR video.
# Pause video
if cv2.waitKey(10) & 0xFF == ord('s'): 
      break
  else:  
    break
# Display video
cv2.imshow("Result",slide)
vc.release()
