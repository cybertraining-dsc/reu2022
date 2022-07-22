#!/usr/bin/env python
# coding: utf-8

# # MNIST with Convolutional Neural Networks

# ## Prerequisites
# 
# Install the following packages



try:
    from cloudmesh.common.StopWatch import StopWatch
except:  # noqa: E722
    get_ipython().system(' pip install cloudmesh-common')
    from cloudmesh.common.StopWatch import StopWatch


# ## Import Libraries



# from __future__ import absolute_import
# from __future__ import division
# from __future__ import print_function
StopWatch.start('total')
StopWatch.start('import')
import numpy as np
from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout
from keras.layers import Conv2D, MaxPooling2D, Flatten, AveragePooling2D
from keras.utils import to_categorical, plot_model
from keras.datasets import mnist
StopWatch.stop('import')
StopWatch.progress(0)


# ## Download Data and Pre-Process



StopWatch.start('data-load')
(x_train, y_train), (x_test, y_test) = mnist.load_data()
StopWatch.stop('data-load')
StopWatch.progress(20)
num_labels = len(np.unique(y_train))

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

image_size = x_train.shape[1]
x_train = np.reshape(x_train,[-1, image_size, image_size, 1])
x_test = np.reshape(x_test,[-1, image_size, image_size, 1])
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

input_shape = (image_size, image_size, 1)
print(input_shape)
batch_size = 128
kernel_size = 3
pool_size = 2
filters = 64
dropout = 0.2
StopWatch.progress(40)


# ## Define Model



model = Sequential()
model.add(Conv2D(filters=filters,
                 kernel_size=kernel_size,
                 activation='relu',
                 input_shape=input_shape,
                 padding='same'))
model.add(MaxPooling2D(pool_size))
model.add(Conv2D(filters=filters,
                 kernel_size=kernel_size,
                 activation='relu',
                 input_shape=input_shape,
                 padding='same'))
model.add(MaxPooling2D(pool_size))
model.add(Conv2D(filters=filters,
                 kernel_size=kernel_size,
                 activation='relu',
                 padding='same'))
model.add(MaxPooling2D(pool_size))
model.add(Conv2D(filters=filters,
                 kernel_size=kernel_size,
                 activation='relu'))
model.add(Flatten())
model.add(Dropout(dropout))
model.add(Dense(num_labels))
model.add(Activation('softmax'))
model.summary()
plot_model(model, to_file='cnn-mnist.png', show_shapes=True)
StopWatch.progress(60)


# # Train



StopWatch.start('compile')
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
StopWatch.stop('compile')
# train the network
StopWatch.start('train')
model.fit(x_train, y_train, epochs=10, batch_size=batch_size)
StopWatch.stop('train')
StopWatch.progress(80)


# ## Test



loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy: %.1f%%" % (100.0 * acc))
StopWatch.stop('total')
StopWatch.progress(100)






