import cv2
import numpy as np

video_url = r"c:\Users\a\Desktop\CNN\IMAGES\red_rose.mp4"
cap = cv2.VideoCapture(video_url)

resize_factor = 0.5  # Adjust this value to scale the frame (e.g., 0.5 for half the size)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, None, fx=resize_factor, fy=resize_factor, interpolation=cv2.INTER_AREA)
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define red color range
    low_red = np.array([161, 155, 84])  
    high_red = np.array([179, 255, 255])

    # Create mask and extract red parts
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

    # Display resized frames
    cv2.imshow("Frame", frame)
    cv2.imshow("Red", red)
    
    key = cv2.waitKey(1)
    if key == 27:  # Press 'ESC' to exit
        break

cap.release()
cv2.destroyAllWindows()
