import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, ZeroPadding2D, Conv2D, MaxPooling2D, Flatten
from sklearn.preprocessing import label_binarize
from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model

#x,y = np.load('trainset.npz')
train = np.load('/Users/SatoshiYokoyama/D-HACKS/face_dataset/trainset.npz')

#print(train['data'].shape)
idx = np.random.permutation(range(train['data'].shape[0]))
x_train = train['data']
x_train = x_train.reshape([x_train.shape[0],3,120,120])
y_train = train['label']
y_train = label_binarize(y_train,classes=range(7))


model = Sequential()

model.add(Conv2D(32,(7,7),input_shape=(3,120,120),padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64,(5,5),padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(1024,activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(7,activation='softmax'))

o = keras.optimizers.SGD(lr=0.0001)
model.compile(loss='categorical_crossentropy', optimizer=o, metrics=['accuracy'])

#print(x_train.shape,y_train.shape)
model.fit(x_train/255., y_train.astype('float32') ,epochs=200, batch_size=4, shuffle=True)

model.save("cnn_d1.h5")
