#coding:utf-8
import numpy as np
import cv2

count = 1

cap = cv2.VideoCapture('/Users/SatoshiYokoyama/Movies/Logitech Webcam/Video 10.mov')

#ret, frame = cap.read()

while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    cv2.imwrite('/Users/SatoshiYokoyama/D-HACKS/face_dataset/face8_1/face8_'+str(count)+'.jpg',frame)
    count += 1

#1=gaku/2=quantan/3=yokoyama/4=hirono/5=heart/6=not_face/7=people
cap.release()
cv2.destroyAllWindows()
