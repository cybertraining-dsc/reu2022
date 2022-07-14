#!/usr/bin/env python
# coding: utf-8

# # MNIST with Recurrent Neural Networks
# This program runs in about 46.033 seconds (Windows 11, i7, 16 GB)

# ## Prerequisites
# 
# Install the following packages



try:
    from cloudmesh.common.StopWatch import StopWatch
except:  # noqa: E722
    get_ipython().system(' pip install cloudmesh-common')
    from cloudmesh.common.StopWatch import StopWatch


# ## Import Libraries



StopWatch.start("total")
StopWatch.start("import")
StopWatch.progress(0)

import numpy as np    # noqa: E402
# import tensorflow as tf
from keras.models import Sequential    # noqa: E402
from keras.layers import Dense, Activation, SimpleRNN    # noqa: E402
from keras.utils import to_categorical, plot_model    # noqa: E402
from keras.datasets import mnist    # noqa: E402
from cloudmesh.common.StopWatch import StopWatch    # noqa: E402

StopWatch.stop("import")
StopWatch.progress(7)


# ## Download Data and Pre-Process



StopWatch.start("data-load")
(x_train, y_train), (x_test, y_test) = mnist.load_data()
StopWatch.stop("data-load")
StopWatch.progress(8)

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
StopWatch.progress(9)

input_shape = (image_size, image_size)
batch_size = 128
units = 256
dropout = 0.2


# ## Define Model



StopWatch.start("compile")
model = Sequential()
model.add(SimpleRNN(units=units,
                    dropout=dropout,
                    input_shape=input_shape, return_sequences=True))
model.add(SimpleRNN(units=units,
                    dropout=dropout,
                    return_sequences=True))
model.add(SimpleRNN(units=units,
                    dropout=dropout,
                    return_sequences=False))
model.add(Dense(num_labels))
model.add(Activation('softmax'))
model.summary()
plot_model(model, to_file='rnn-mnist.png', show_shapes=True)


model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
StopWatch.stop("compile")
StopWatch.progress(10)


# ## Train



StopWatch.start("train")
model.fit(x_train, y_train, epochs=1, batch_size=batch_size)
StopWatch.stop("train")
StopWatch.progress(95)


# ## Test



StopWatch.start("evaluate")
loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy: %.1f%%" % (100.0 * acc))
StopWatch.stop("evaluate")

StopWatch.stop("total")
StopWatch.benchmark()
StopWatch.progress(100)

