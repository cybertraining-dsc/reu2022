#!/usr/bin/env python
# coding: utf-8

# # Multi-Layer Perceptron with MNIST

# ## Pre-requisites
# 
# Install the following Python packages
# 
# 1. cloudmesh-installer
# 2. cloudmesh-common



get_ipython().system(' pip3 install cloudmesh-installer')
get_ipython().system(' pip3 install cloudmesh-common')


# ## Sample MLP with Tensorflow Keras



from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import time 

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.utils import to_categorical, plot_model
from keras.datasets import mnist
#import pydotplus
from keras.utils.vis_utils import model_to_dot
#from keras.utils.vis_utils import pydot


from cloudmesh.common.StopWatch import StopWatch

StopWatch.start("data-load")
(x_train, y_train), (x_test, y_test) = mnist.load_data()
StopWatch.stop("data-load")

num_labels = len(np.unique(y_train))


y_train = to_categorical(y_train)
y_test = to_categorical(y_test)


image_size = x_train.shape[1]
input_size = image_size * image_size


x_train = np.reshape(x_train, [-1, input_size])
x_train = x_train.astype('float32') / 255
x_test = np.reshape(x_test, [-1, input_size])
x_test = x_test.astype('float32') / 255

batch_size = 128
hidden_units = 512
dropout = 0.45

model = Sequential()
model.add(Dense(hidden_units, input_dim=input_size))
model.add(Activation('relu'))
model.add(Dropout(dropout))
model.add(Dense(hidden_units))
model.add(Activation('relu'))
model.add(Dropout(dropout))
model.add(Dense(hidden_units))
model.add(Activation('relu'))
model.add(Dropout(dropout))
model.add(Dense(hidden_units))
model.add(Activation('relu'))
model.add(Dropout(dropout))
model.add(Dense(num_labels))
model.add(Activation('softmax'))
model.summary()
plot_model(model, to_file='mlp-mnist.png', show_shapes=True)

StopWatch.start("compile")
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
StopWatch.stop("compile")
StopWatch.start("train")
model.fit(x_train, y_train, epochs=5, batch_size=batch_size)
StopWatch.stop("train")

StopWatch.start("test")
loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy: %.1f%%" % (100.0 * acc))
StopWatch.stop("test")

StopWatch.benchmark()



# # REFERENCES
# 
# 1. [Adavnced Keras Deep Learning Book](https://github.com/PacktPublishing/Advanced-Deep-Learning-with-Keras)
