# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:11:59 2020

@author: Access
"""
import numpy as np
import tensorflow as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D
import os
import cv2
import random

Datadir="C:/Users/Access/Board Detection App/"
path = os.path.join(Datadir, "Test")
labels=[]
training_data=[]
img_size=30

def create_model_pieces():
    model = Sequential()

    model.add(Conv2D(64, (5, 5), input_shape=(30,30,1)))
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
    return model


model=create_model_pieces()
model.load_weights('./model_weights_pieces')
def create_training_data():
    
    for img in os.listdir(path):
        img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
        #img_array=cv2.equalizeHist(img_array)
        img_array=cv2.resize(img_array,(img_size,img_size))
        training_data.append([img_array])
        
    X=[]
    for feature in training_data:
        X.append(feature)
        
    X=np.array(X).reshape(-1,img_size,img_size,1)
    return X

X_test1= create_training_data()
X_test=X_test1/255.0
y_predict=model.predict(X_test)
y_predict=y_predict.argmax(axis=1)
for i in range(len(X_test)):
    image =X_test1[i].reshape(30,30)
    cv2.imwrite("C:/Users/Access/Board Detection App/Test_result/file"+str(i)+"-"+'KQRBNPkqrbnp'[y_predict[i]]+".png",image)
    