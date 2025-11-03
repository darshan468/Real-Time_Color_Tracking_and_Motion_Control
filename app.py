import cv2   # OpenCV library for computer vision tasks
import imutils  # help for resizing images

# Red color in hsv value
redLower = (78, 50, 150)
redUpper = (179, 255, 255)

cam = cv2.VideoCapture(0) # Initialize the webcam

while True:
    (grabbed, frame) = cam.read() # Capture frame-by-frame
    
    frame = imutils.resize(frame, width=600)   # Resize the frame to width of 600 pixels
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)   # Apply Gaussian blur to the frame
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    # Convert the frame from BGR to HSV color space
    
    mask = cv2.inRange(hsv, redLower, redUpper)
    mask = cv2.erode(mask, None, iterations=2)   # Erode to remove small blocks
    mask = cv2.dilate(mask, None, iterations=2)  # Morphological operations to remove small blocks noisy
    
    # Contour detection -  finds the outer boundary or outline of an object in an image
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]   # Find contours in the mask
    
    center = None
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea) 
        ((x, y), radius) = cv2.minEnclosingCircle(c) 
        M = cv2.moments(c)
        
        # ROBUSTNESS CHECK - A robustness check is a way to see if the main results of a study or analysis still hold true even if you change the methods, assumptions, or data slightly
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])) 
        
        # Only for radius point command line
        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
          
          # Decision making based on the position and size of the detected object  
            if radius > 250:
                print("Stop")
            else:
                if(center[0] < 150):
                    print("Left")
                elif(center[0] > 450):
                    print("Right")
                elif(radius < 250):
                    print("Front")
                else:
                    print("Stop")
                    
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
            break

cam.release()
cv2.destroyAllWindows()