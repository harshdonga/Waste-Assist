# -*- coding: utf-8 -*-
"""
Created on 10:12:59 2019

@author: Harsh
"""

## MANIP LIB  ##
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import cv2

##  DL LIBS  ##
import keras
import tensorflow as tf

##  MODELS PREP LIB ##
from keras.models import Sequential, load_model
from keras.layers import Dense, MaxPooling2D, Conv2D, Flatten, Dropout
from keras.losses import categorical_crossentropy
from keras.optimizers import adam, sgd
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint

from PIL import Image

h=60
b=30

train = ImageDataGenerator(rotation_range=45,width_shift_range=0.2,height_shift_range=0.2,horizontal_flip=True).flow_from_directory('C:/Users/Harsh/Desktop/Trials/WASTE/DATASET/TRAIN',
                             target_size=(h,b),
                            classes=['O', 'R'],
                            batch_size=100)

test = ImageDataGenerator().flow_from_directory('C:/Users/Harsh/Desktop/Trials/WASTE/DATASET/TEST',
                                                 target_size= (h,b),
                                                 classes= ['O', 'R'],
                                                 batch_size = 100)


def make_model():

    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), padding='same', activation='relu', input_shape=(h,b,3)))
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))

    model.add(Dropout(0.25))
    model.add(Flatten())

    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.5))

    model.add(Dense(2, activation='softmax'))
    model.summary()

    return model


def usemodel(path):

    model = load_model('best_waste_classifier.h5')
    pic = plt.imread(path)
    pic = cv2.resize(pic, (b,h))
    pic = np.expand_dims(pic, axis=0)
    classes = model.predict_classes(pic)

    return classes

model = make_model()

checkpoint = ModelCheckpoint('best_waste_classifier.h5',
                             monitor='val_loss',
                             verbose=0,
                             save_best_only=True,
                             mode='auto')


model.compile(loss='categorical_crossentropy', optimizer=adam(lr=1.0e-4), metrics=['accuracy'])

from math import ceil
n_points = len(test)
batch_size = 100

model= model.fit_generator(train,
                           validation_data=test,
                           steps_per_epoch=15,
                           validation_steps=5,
                           epochs=30,
                           verbose=1,
                           callbacks=[checkpoint])

print(usemodel('C:/Users/Harsh/Desktop/Trials/WASTE/DATASET/TEST/'))
