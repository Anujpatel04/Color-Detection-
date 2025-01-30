# Only Green Color 

import cv2
import numpy as np

video_url = r"c:\Users\a\Desktop\CNN\IMAGES\green_lraf.mp4"
cap = cv2.VideoCapture(video_url)
while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    
    # Green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

    cv2.imshow("Frame", frame) 
    cv2.imshow('Green', green)
    
    
    key = cv2.waitKey(1)
    if key ==27:
        break




