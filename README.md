# Face Detection Using Python with OpenCV

This project demonstrates basic face detection using the OpenCV library in Python. It uses a pre-trained Haar Cascade classifier to detect faces in an input image and draws rectangles around detected faces.

## Requirements

- Python 3.x
- OpenCV

You can install OpenCV using pip:

```bash
pip install opencv-python

Usage
Import the OpenCV library:
import cv2

Use the pre-trained classifier from OpenCV:
face_cascade = cv2.CascadeClassifier("/content/haarcascade_frontalface_default.xml")

Upload the input image:
img = cv2.imread('/content/Screenshot 2024-04-28 194655.png')

Perform face detection:
faces = face_cascade.detectMultiScale(img, 1.1, 4)

Draw rectangles around detected faces:
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

Export the resulting image:
cv2.imwrite("abhi.png", img)
print("Image successfully exported")
