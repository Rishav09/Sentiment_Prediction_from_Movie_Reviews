#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:07:28 2018

@author: rishav
"""

import numpy
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense,Flatten
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence

seed=7
numpy.random.seed(seed)

top_words=5000
(X_train,y_train),(X_test,y_test)=imdb.load_data(num_words=top_words)

max_words=500
X_train=sequence.pad_sequences(X_train,maxlen=max_words)
X_test=sequence.pad_sequences(X_test,maxlen=max_words)

model=Sequential()
model.add(Embedding(top_words,32,input_length=max_words))
model.add(Flatten())
model.add(Dense(250,activation='relu'))
model.add(Dense(1,activation='relu'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
print(model.summary())
model.fit(X_train,y_train,validation_data=(X_test,y_test),epochs=2,batch_size=128,verbose=1)
scores=model.evaluate(X_test,y_test,verbose=0)
print("Accuracy : %.2f%%" % (scores[1]*100))

