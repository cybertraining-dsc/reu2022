#!/usr/bin/env python
# coding: utf-8

# # MLP + LSTM with MNIST



try:
    from cloudmesh.common.StopWatch import StopWatch
except:  # noqa: E722
    get_ipython().system(' pip install cloudmesh-common')
    from cloudmesh.common.StopWatch import StopWatch




StopWatch.start("total")
StopWatch.start("import")
StopWatch.progress(0)

import numpy as np    # noqa: E402
# import tensorflow as tf
from keras.models import Sequential    # noqa: E402
from keras.layers import Dense, Activation, SimpleRNN, InputLayer, LSTM, Dropout    # noqa: E402
from keras.utils import to_categorical, plot_model    # noqa: E402
from keras.datasets import mnist    # noqa: E402
from cloudmesh.common.StopWatch import StopWatch    # noqa: E402

StopWatch.stop("import")
StopWatch.progress(1)


# ## Data Pre-Process



StopWatch.start("data-load")
(x_train, y_train), (x_test, y_test) = mnist.load_data()
StopWatch.stop("data-load")
StopWatch.progress(2)


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
StopWatch.progress(3)

input_shape = (image_size, image_size)
batch_size = 128
units = 256
dropout = 0.2


# ## Define Model



StopWatch.start("compile")
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


model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
StopWatch.stop("compile")
StopWatch.progress(4)


# ## Train



StopWatch.start("train")
model.fit(x_train, y_train, epochs=30, batch_size=batch_size)
StopWatch.stop("train")
StopWatch.progress(99)


# ## Test



StopWatch.start("evaluate")
loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy: %.1f%%" % (100.0 * acc))
StopWatch.stop("evaluate")

StopWatch.stop("total")
StopWatch.benchmark()
StopWatch.progress(100)


# # References
# 
# 1. [Advance Deep Learning with Keras](https://github.com/PacktPublishing/Advanced-Deep-Learning-with-Keras)
