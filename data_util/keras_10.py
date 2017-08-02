
import gpu_config
gpu_config.set_tensorflow([0])

import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, ZeroPadding2D, Conv2D, MaxPooling2D, Flatten, BatchNormalization, GlobalAveragePooling2D
from sklearn.preprocessing import label_binarize
from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
from sklearn.cross_validation import train_test_split
from keras.callbacks import ModelCheckpoint




#x,y = np.load('trainset.npz')
train = np.load('./trainset2.npz')
test = np.load('./testset2.npz')
valid = np.load('./validset2.npz')

#print(train['data'].shape)
x_train = train['data']
x_train = x_train.reshape([x_train.shape[0], 120, 120, 3])
y_train = train['label']
y_train = label_binarize(y_train,classes=range(9))

x_test = test['data']
x_test = x_test.reshape([x_test.shape[0], 120, 120, 3])
y_test = test['label']
y_test = label_binarize(y_test,classes=range(9))
#x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.2)

x_valid = valid['data']
x_valid = x_valid.reshape([x_valid.shape[0],120,120,3])
y_valid = valid['label']
y_valid = label_binarize(y_valid,classes=range(9))

print x_train.shape

model = Sequential()

model.add(Conv2D(32,(3,3),input_shape=(120,120,3),padding='valid'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64,(3,3),padding='valid'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(128,(3,3),padding='valid'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(256,(3,3),padding='valid'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(512,(3,3),padding='valid'))
model.add(Activation('relu'))

model.add(GlobalAveragePooling2D())

model.add(Dense(1024))
model.add(Activation('relu'))

model.add(Dropout(0.2))

model.add(Dense(1024))
model.add(Activation('relu'))

model.add(Dense(9,activation='softmax'))

model.summary()
o = keras.optimizers.Adam(lr=0.0003)
model.compile(loss='categorical_crossentropy', optimizer=o, metrics=['accuracy'])
checkpointer = ModelCheckpoint(filepath='cnn_d2.h5', verbose=1, save_best_only=True)
#print(x_train.shape,y_train.shape)
model.fit(x_train/255., y_train.astype('float32') , callbacks=[checkpointer], validation_data=[x_valid/255., y_valid.astype("float32")], epochs=2, batch_size=16, shuffle=True)
model.save("cnn_d2.h5")

score=model.evaluate(x_test/255., y_test.astype('float32'),verbose=1, batch_size=16)
print score[0],score[1]
#model.save("cnn_d2.h5")
