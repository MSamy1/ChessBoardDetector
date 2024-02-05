# -*- coding: utf-8 -*-
"""
Created on Fri May  1 17:10:16 2020

@author: Access
"""


import tensorflow as tf
import numpy as np
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D
from tensorflow.python.keras.callbacks import TensorBoard
import matplotlib.pyplot as plt
import pickle
import time
name = "CNN-64x2dense-{}".format(int(time.time()))
tensorboard= TensorBoard(log_dir='log\{}'.format(name))
pickle_in = open("X.pickle","rb")
X = pickle.load(pickle_in)

pickle_in = open("y.pickle","rb")
y = pickle.load(pickle_in)
y=np.array(y)

X = X/255.0

model = Sequential()

model.add(Conv2D(64, (5, 5), input_shape=X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))



model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors

model.add(Dense(64))
model.add(Dropout(0.2))

model.add(Dense(12))
model.add(Activation('softmax'))

model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),optimizer='adam',metrics=['accuracy'])

model.fit(X, y, batch_size=30,epochs=40, validation_split=0.1,callbacks=[tensorboard])

y_predict=model.predict(X[100:101])
image=X[100:101]
image=image.reshape((30,30))
plt.imshow(image)  
plt.show()
