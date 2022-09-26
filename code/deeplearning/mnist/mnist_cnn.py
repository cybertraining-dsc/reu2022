#!/usr/bin/env python
# coding: utf-8

# # MNIST with Convolutional Neural Networks
# 
# This program runs in about 468.937 seconds (Windows 11, Intel i7, 16 GB)

# ## Pre-requisites
# 
# Install the following Python packages
# 
# 1. cloudmesh-installer
# 2. cloudmesh-common



from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.Shell import Shell    # noqa: E402
from cloudmesh.common.variables import Variables

gpuname = Shell.run('nvidia-smi --list-gpus')
v = Variables()
gpuname = v['currentgpu']
filename = Shell.map_filename(f'~/reu2022/code/deeplearning/mnist/mnist_cnn-{gpuname}.log').path


# ## Exporting Output Graphs



def save(graph, filename):
    if os.path.exists("images"):
        pass
    else:
        Shell.mkdir("images")
    plot_model(graph, to_file=f'images/{filename}.png', show_shapes=True)
    plot_model(graph, to_file=f'images/{filename}.pdf', show_shapes=True)


# ## Import Libraries



StopWatch.start('total')
StopWatch.start('import')
StopWatch.progress(0, filename=filename)

import os    # noqa: E402
import cpuinfo    # noqa: E402
import numpy as np    # noqa: E402
from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout    # noqa: E402
from keras.layers import Conv2D, MaxPooling2D, Flatten, AveragePooling2D    # noqa: E402
from keras.utils import to_categorical, plot_model    # noqa: E402
from keras.datasets import mnist    # noqa: E402
from cloudmesh.common.systeminfo import os_is_windows    # noqa: E402
from cloudmesh.common.variables import Variables

StopWatch.stop('import')
StopWatch.progress(1, filename=filename)


# ## Data Load



StopWatch.start('data-load')

(x_train, y_train), (x_test, y_test) = mnist.load_data()

StopWatch.stop('data-load')
StopWatch.progress(2, filename=filename)


# ## Data Pre-Process



StopWatch.start("data-pre-process")

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

StopWatch.stop("data-pre-process")
StopWatch.progress(3, filename=filename)


# ## Define Model



StopWatch.start("compile")

batch_size = 128
kernel_size = 3
pool_size = 2
filters = 64
dropout = 0.2

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
save(model, 'mnist_cnn')

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

StopWatch.stop("compile")
StopWatch.progress(4, filename=filename)


# # Train



StopWatch.start('train')

model.fit(x_train, y_train, epochs=5, batch_size=batch_size)

StopWatch.stop('train')
StopWatch.progress(99, filename=filename)


# ## Test



StopWatch.start('test')

loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy: %.1f%%" % (100.0 * acc))

StopWatch.stop('test')
StopWatch.stop('total')
StopWatch.progress(100, filename=filename)

if os_is_windows():
    user = os.environ["USERNAME"]
else:
    try:
        user = os.environ['USER']
    except:  # noqa: E722
        user = os.system('basename $HOME')

# try:
#     gpuname = ''
#     for line in open('mnist_cnn.log', 'r'):
#         if 'GPU' in line and line[-2] == ')':
#             gpuname = gpuname + line[:line.find('(')] + '\n'
# except:  # noqa: E722
#     gpuname = cpuinfo.get_cpu_info()['brand_raw']


v = Variables()
host = v['host']
user = v['user']
cpu = v['cpu']
gpu = v['gpu']

tag = 'mnist_cnn'
#tag = 'mnist_cnn-user-host-gpu-cpu'

StopWatch.benchmark(tag=tag, node=gpuname, user=user, filename=filename)

