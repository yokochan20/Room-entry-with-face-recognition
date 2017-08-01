# -*- coding: utf-8 -*-

import cv2
import sys
import os
import shutil
import random
#HAAR分類器の顔検出用の特徴量
cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml"
c = 1
e = 1
count = 580
for x in range(20):
	image_path = '/Users/SatoshiYokoyama/D-HACKS/lfw 600/'+'lfw'+str(count)+'.jpg'

	color = (255, 255, 255) #白

#ファイル読み込み
	image = cv2.imread(image_path)
#グレースケール変換
	image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#カスケード分類器の特徴量を取得する
	cascade = cv2.CascadeClassifier(cascade_path)

#物体認識（顔認識）の実行
	facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

	print ("face rectangle")
	print (facerect)
	
	if len(facerect) > 0:
		path = os.path.splitext(image_path)
		dir_path = path[0] + '_face'
		if os.path.isdir(dir_path):
			shutil.rmtree(dir_path)
		os.mkdir(dir_path)
		e += 1
		print(e)

#i = 0;
	for rect in facerect:
	#顔だけ切り出して保存
		x = rect[0]
		y = rect[1]
		width = rect[2]
		height = rect[3]
		dst = image[y:y+height, x:x+width]
		new_image_path = dir_path + '/' +'f5_1_'+ str(c) + path[1];
		cv2.imwrite(new_image_path, dst)
		count =count + 1
		c = c + 1

