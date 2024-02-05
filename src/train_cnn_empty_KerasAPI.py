#Keras Functional API
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

pickle_in = open("X.pickleempty","rb")
Xe = pickle.load(pickle_in)

pickle_in = open("y.pickleempty","rb")
ye = pickle.load(pickle_in)
ye=np.array(ye)

Xe = Xe/255.0
pieces_model=lm.create_model_pieces()
Ye_pieces_predict=pieces_model.predict(Xe)


#Create CNN model
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
model.fit([Xe,Ye_pieces_predict],ye,batch_size=30,epochs=15, validation_split=0.2)


y_predict=model.predict([Xe[100:140],Ye_pieces_predict[100:140]])
image=Xe[100:101]
image=image.reshape((30,30))
plt.imshow(image)  
plt.show()
model.save_weights('./model_weights_empty')
