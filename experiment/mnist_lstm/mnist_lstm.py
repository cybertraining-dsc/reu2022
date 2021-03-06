#!/usr/bin/env python
# coding: utf-8

# # Simple LSTM with MNIST



try:
    from cloudmesh.common.StopWatch import StopWatch
except:  # noqa: E722
    get_ipython().system(' pip install cloudmesh-common')
    from cloudmesh.common.StopWatch import StopWatch

# from __future__ import absolute_import
# from __future__ import division
# from __future__ import print_function
StopWatch.start('total')
StopWatch.start('import')
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, SimpleRNN, InputLayer, LSTM
from tensorflow.keras.utils import to_categorical, plot_model
from tensorflow.keras.datasets import mnist
from cloudmesh.common.StopWatch import StopWatch
StopWatch.stop('import')
StopWatch.progress(0)


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
StopWatch.progress(20)


# ## Define Model



StopWatch.progress(40)
StopWatch.start("compile")
model = Sequential()
model.add(LSTM(units=units,                      
                     input_shape=input_shape,
                     return_sequences=True))
model.add(LSTM(units=units, 
                     dropout=dropout,                      
                     return_sequences=True))
model.add(LSTM(units=units, 
                     dropout=dropout,                      
                     return_sequences=False))
model.add(Dense(num_labels))
model.add(Activation('softmax'))
model.summary()
plot_model(model, to_file='rnn-mnist.png', show_shapes=True)

StopWatch.progress(60)
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
StopWatch.stop("compile")


# ## Train



StopWatch.progress(80)
StopWatch.start("train")
model.fit(x_train, y_train, epochs=1, batch_size=batch_size)
StopWatch.stop("train")


# ## Test



StopWatch.start("evaluate")
loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy: %.1f%%" % (100.0 * acc))
StopWatch.stop("evaluate")

StopWatch.benchmark()
StopWatch.progress(100)

