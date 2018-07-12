# -*- coding: utf-8 -*-
import cv2

face_patterns = cv2.CascadeClassifier('C:/Users/Administrator/Downloads/opencv/build/etc/haarcascades/haarcascade_frontalface_default.xml')

sample_image = cv2.imread('C:/Users/Administrator/Desktop/123.jpg')

faces = face_patterns.detectMultiScale(sample_image,scaleFactor=1.2,minNeighbors=5,minSize=(100, 100))

for (x, y, w, h) in faces:
    cv2.rectangle(sample_image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imwrite('C:/Users/Administrator/Desktop/123.png', sample_image);