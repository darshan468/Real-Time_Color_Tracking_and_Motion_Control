### Real-Time Color Tracking and Basic Command System

# 🚀 Project Overview
This Python application utilizes the OpenCV library to perform real-time object tracking from a live webcam feed. The system is configured to isolate and track objects within a specific red HSV color range.

# Key Functionality
Live Video Processing: Continuously captures frames from the webcam for immediate analysis.

Color Segmentation: Converts the image to the HSV color space for reliable color-based isolation, generating a binary mask.

Contour Detection: Identifies the largest contiguous red region, calculates its bounding circle's center (centroid) and radius (size).

Simple Control Logic: Translates the object's physical appearance (position and size) into basic console commands:

"Left" / "Right": Based on the object's horizontal position.

"Stop": Triggered if the object is too large (close) or centered/far.

"Front": Triggered when the object is centered and within a defined distance range.

# Customization
Change Target Color: Modify the redLower and redUpper HSV tuples to track a different color.

Camera Index: If the default cv2.VideoCapture(0) fails, try changing the index to 1 or -1 to connect to an external or alternative camera.

Tuning Sensitivity: Adjust the positional thresholds (150 and 450) and the radius thresholds (> 10, > 250) to fine-tune the control logic's response to the object's movement and proximity.
