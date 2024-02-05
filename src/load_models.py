#Creating and loading models

import numpy as np
import tensorflow as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D
import os
import cv2


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
    model.load_weights('./model_weights_pieces').expect_partial()
    return model



def create_model_empty():
    modele = Sequential()
    
    modele.add(Conv2D(64, (5, 5), input_shape=(30,30,1)))
    modele.add(Activation('relu'))
    modele.add(MaxPooling2D(pool_size=(2, 2)))
    
    modele.add(Conv2D(64, (3, 3)))
    modele.add(Activation('relu'))
    modele.add(MaxPooling2D(pool_size=(2, 2)))
    
    
    modele.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
    
    modele.add(Dense(64))
    
    modele.add(Dense(1))
    modele.add(Activation('sigmoid'))
    
    modele.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
    modele.load_weights('./model_weights_empty').expect_partial()
    return modele
    


# #Train the model with more data
# Xe = Xe/255.0
# modele=create_model_empty()
# modele.fit(Xe, Ye, batch_size=30,epochs=30, validation_split=0.2)
# modele.save_weights('./model_weights_empty')



#Train the model with more data
# X = X/255.0
# model=create_model_pieces()
# model.fit(X, Y, batch_size=30,epochs=30, validation_split=0.2)
# model.save_weights('./model_weights_pieces')
