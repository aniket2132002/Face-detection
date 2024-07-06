
"""Face detection using python with OpenCV



Original file is located at
    https://colab.research.google.com/drive/1acJOc85xYtEVop4kj9Ccjzrsj6ISNzin

### **Face Detection Usig puthon with OpenCV**

Import the OpenCv library
"""

import cv2

"""use pre-trained classifier From OpenCV"""

face_cascade = cv2.CascadeClassifier("/content/haarcascade_frontalface_default.xml")

"""upload image Input"""

img=cv2.imread('/content/Screenshot 2024-04-28 194655.png')

"""perform face detection"""

faces = face_cascade.detectMultiScale(img, 1.1 ,4)

"""here i draw rectangle"""

for (x, y, w, h) in faces:
  cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

"""exporting the image file"""

#export the result
cv2.imwrite("abhi.png", img)
print("image successfully exported")