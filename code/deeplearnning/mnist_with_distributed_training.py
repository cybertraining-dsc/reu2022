#!/usr/bin/env python
# coding: utf-8

# # Distributed Training for MNIST



# get_ipython().system('pip3 install cloudmesh-installer')
# get_ipython().system('pip3 install cloudmesh-common')




from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, SimpleRNN, InputLayer, LSTM, Dropout
from tensorflow.keras.utils import to_categorical, plot_model
from tensorflow.keras.datasets import mnist
from cloudmesh.common.StopWatch import StopWatch


# ## Data Pre-Process



StopWatch.start("data-load")
(x_train, y_train), (x_test, y_test) = mnist.load_data()
StopWatch.stop("data-load")


StopWatch.start("data-pre-process")
num_labels = len(np.unique(y_train))


y_train = to_categorical(y_train)
y_test = to_categorical(y_test)


image_size = x_train.shape[1]
x_train = np.reshape(x_train,[-1, image_size, image_size])
x_test = np.reshape(x_test,[-1, image_size, image_size])
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255
StopWatch.stop("data-pre-process")

input_shape = (image_size, image_size)
batch_size = 128
units = 256
dropout = 0.2


# ## Define Model

# Here we use the Tensorflow distributed training components to train the model in multiple CPUs or GPUs. In the Colab instance multiple GPUs are not supported. Hence, the training must be done in the device type 'None' when selecting the 'runtime type' from Runtime menu. To run with multiple-GPUs no code change is required. [Learn more about distributed training](https://www.tensorflow.org/guide/distributed_training).



StopWatch.start("compile")
strategy = tf.distribute.MirroredStrategy()
with strategy.scope():
  model = Sequential()
  # LSTM Layers
  model.add(LSTM(units=units,                      
                      input_shape=input_shape,
                      return_sequences=True))
  model.add(LSTM(units=units, 
                      dropout=dropout,                      
                      return_sequences=True))
  model.add(LSTM(units=units, 
                      dropout=dropout,                      
                      return_sequences=False))
  # MLP Layers
  model.add(Dense(units))
  model.add(Activation('relu'))
  model.add(Dropout(dropout))
  model.add(Dense(units))
  model.add(Activation('relu'))
  model.add(Dropout(dropout))
  # Softmax_layer
  model.add(Dense(num_labels))
  model.add(Activation('softmax'))
  model.summary()
  plot_model(model, to_file='rnn-mnist.png', show_shapes=True)
  
  print("Number of devices: {}".format(strategy.num_replicas_in_sync))

  model.compile(loss='categorical_crossentropy',
                optimizer='sgd',
                metrics=['accuracy'])
StopWatch.stop("compile")


# ## Train



StopWatch.start("train")
model.fit(x_train, y_train, epochs=30, batch_size=batch_size)
StopWatch.stop("train")


# ## Test



StopWatch.start("evaluate")
loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy: %.1f%%" % (100.0 * acc))
StopWatch.stop("evaluate")

StopWatch.benchmark()


# # References
# 
# 1. [Advance Deep Learning with Keras](https://github.com/PacktPublishing/Advanced-Deep-Learning-with-Keras)
# 2. [Distributed With Tensorflow](https://www.tensorflow.org/guide/distributed_training)
# 3. [Keras with Tensorflow Distributed Training](https://keras.io/guides/distributed_training/)
