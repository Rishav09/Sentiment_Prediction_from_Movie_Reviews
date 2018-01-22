#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 09:26:23 2018

@author: rishav
"""
import numpy
from keras.datasets import imdb
from matplotlib import pyplot

(X_train,y_train),(X_test,y_test)=imdb.load_data()
X=numpy.concatenate((X_train,X_test),axis=0)
y=numpy.concatenate((y_train,y_test),axis=0)

print("Training Data: ")
print(X.shape)
print(y.shape)

print("Classes: ")
print(numpy.unique(y))
print("Number of Words: ")
print(len(numpy.unique(numpy.hstack(X))))

print("Review length: ")
result=map(len,X)
print("Mean %.2f words (%f)" % (numpy.mean(result),numpy.std(result)))
pyplot.subplot(121)
pyplot.boxplot(result)
pyplot.subplot(122)
pyplot.hist(result)
pyplot.show()