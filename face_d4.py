# -*- coding: utf-8 -*-

import cv2
import sys
import os
import shutil
import random
#HAAR分類器顔検出用の特徴量
#cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
#cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"
cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml"
#cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt_tree.xml"
c = 200
e = 1
for x in range(150):
	count = random.randint(1,1248)
	image_path = '/Users/SatoshiYokoyama/D-HACKS/face_dataset/face5_1/face5_'+str(count)+'.jpg'
	#sys.argv[1]

	color = (255, 255, 255) #白
#color = (0, 0, 0) #黒

#ファイル読み込み
	image = cv2.imread(image_path)
#グレースケール変換
	image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#カスケード分類器の特徴量を取得する
	cascade = cv2.CascadeClassifier(cascade_path)

#顔認識の実行
#objects – 矩形を要素とするベクトル．それぞれの矩形は，検出した物体を含みます
#minSize – 物体が取り得る最小サイズ
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
		new_image_path = dir_path + '/' +'f9_'+ str(c) + path[1];
		cv2.imwrite(new_image_path, dst)
		count =count - 1
		c = c + 1

