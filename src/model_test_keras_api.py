#Keras Functional API Test
from keras.models import Model
from keras.layers import Input
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import concatenate
import numpy as np
import matplotlib.pyplot as plt
import pickle
import time
import load_models as lm
import os
import cv2

Datadir="C:/Users/Access/Board Detection App/"
path = os.path.join(Datadir, "Test")
labels=[]
training_data=[]
img_size=30

def create_model_empty_keras():
    visible = Input(shape=(30,30,1))
    conv1 = Conv2D(64, kernel_size=5, activation='relu')(visible)
    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)
    conv2 = Conv2D(64, kernel_size=3, activation='relu')(pool1)
    pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)
    flat = Flatten()(pool2)
    
    
    
    #Create secondary model for pieces prediction input
    input2=Input(shape=(12,))
    hidden2 = Dense(12, activation='relu')(input2)
    hidden3 = Dense(20, activation='relu')(hidden2)
    hidden4 = Dense(10, activation='relu')(hidden3)
    
    #Merge 2 models
    merge=concatenate([hidden4, flat])
    
    #Interpretation model
    hidden1 = Dense(64, activation='relu')(merge)
    output = Dense(1, activation='sigmoid')(hidden1)
    
    model = Model(inputs=[visible,input2], outputs=output)
    model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
    model.load_weights('./model_weights_empty')
    return model

def create_training_data():
    
    for img in os.listdir(path):
        img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
        #img_array=cv2.equalizeHist(img_array)
        img_array=cv2.GaussianBlur(img_array,(3,3),0)
        img_array=cv2.resize(img_array,(img_size,img_size))
        training_data.append([img_array])
        
    X=[]
    for feature in training_data:
        X.append(feature)
        
    X=np.array(X).reshape(-1,img_size,img_size,1)
    return X

modele=create_model_empty_keras()
X_test1= create_training_data()
X_test=X_test1/255.0
#Create input2 (pieces model output)
pieces_model=lm.create_model_pieces()
x2=pieces_model.predict(X_test)

y_predict=modele.predict([X_test,x2])
y_predict=[round(num.max()) for num in y_predict]
for i in range(len(X_test)):
    image =X_test1[i].reshape(30,30)
    cv2.imwrite("C:/Users/Access/Board Detection App/Test_resulte/"+str(y_predict[i])+"file"+str(i)+"-"+str(y_predict[i])+".png",image)
    