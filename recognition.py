#-*- coding: utf-8 -*-

import sys
import os
import numpy as np
import cv2
import time

from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
from unlock_client import callraspi
from slack_s103 import post_slack

cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml"
cascade = cv2.CascadeClassifier(cascade_path)
color = (255, 255, 255)
cap = cv2.VideoCapture(0)

'''
import h5py
model = h5py.File('cnn_d2.h5', 'r+')
del model['optimizer_weights']
model.close()
'''

model = load_model('cnn_d2.h5')
model.summary()
font = cv2.FONT_HERSHEY_SIMPLEX
color = (255,255,255)

def main():
    while(cap.isOpened()):
        ret, frame = cap.read()
        #face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray,scaleFactor=1.1,
                                         minNeighbors=5,minSize=(100,100),
                                         flags = cv2.CASCADE_SCALE_IMAGE
                                         )
        cv2.imwrite("frontalface.png",frame)
        img=cv2.imread("frontalface.png")
        if len(faces) > 0:
            for rect in faces:
                cv2.rectangle(frame, tuple(rect[0:2]),
                              tuple(rect[0:2] + rect[2:4]),
                              color, thickness=2
                              )
                x = rect[0]
                y = rect[1]
                width = rect[2]
                height = rect[3]
                dst = img[y:y+height, x:x+width]
                cv2.imwrite("output.png", dst)
            i = cv2.imread("output.png")
            im = cv2.cvtColor(cv2.resize(i,(120,120)), cv2.COLOR_BGR2RGB)
            imag = np.array([np.array(im)])
            image  = imag.astype("float")  / 255.

            pre = model.predict_classes(image)
            print(pre[0])
            if pre == 0:
                pre = "gaku"
                callraspi()
                post_slack("gaku")
            elif pre == 1:
                pre ="quantan"
                callraspi()
                post_slack("quantan")
            elif pre == 2:
                pre ="yokochan"
                callraspi()
                post_slack("yokochan")
            elif pre == 3:
                pre ="hirono"
                callraspi()
                post_slack("hirono")
            elif pre == 4:
                pre ="heart"
                callraspi()
                post_slack("heart")
            elif pre == 5:
                pre ="Not human"
            elif pre == 6:
                pre ="Not Member"
            elif pre == 7:
                pre =u"birdmanさん"
                callraspi()
                post_slack(u"birdmanさん")
            else:
                pre =u"cozyさん"
                callraspi()
                post_slack(u"cozyさん")
            cv2.putText(frame,str(pre),(rect[0],rect[1]-10),font,1,color,1,8)
        cv2.imshow("Faces Classification" ,frame)
            #time.sleep(0.4)

        code = cv2.waitKey(1)
        if code == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
