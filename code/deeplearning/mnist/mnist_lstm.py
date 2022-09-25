#!/usr/bin/env python
# coding: utf-8

# # Simple LSTM with MNIST
# 
# This program runs in about 180.064 seconds (Windows 11, Intel i7, 16 GB

# ## Pre-requisites
# 
# Install the following Python packages
# 
# 1. cloudmesh-installer
# 2. cloudmesh-common



from cloudmesh.common.StopWatch import StopWatch


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
StopWatch.progress(0)

import os    # noqa: E402
import cpuinfo  #noqa: E402
import numpy as np  #noqa: E402
from keras.models import Sequential  #noqa: E402
from keras.layers import Dense, Activation, SimpleRNN, InputLayer, LSTM  #noqa: E402
from keras.utils import to_categorical, plot_model  #noqa: E402
from keras.datasets import mnist  #noqa: E402
from cloudmesh.common.systeminfo import os_is_windows    # noqa: E402
from cloudmesh.common.Shell import Shell    # noqa: E402

StopWatch.stop('import')
StopWatch.progress(5)


# ## Data Load



StopWatch.start("data-load")

(x_train, y_train), (x_test, y_test) = mnist.load_data()

StopWatch.stop("data-load")
StopWatch.progress(10)


# ## Data Pre-Process



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
StopWatch.progress(20)


# ## Define Model



StopWatch.start("compile")

input_shape = (image_size, image_size)
batch_size = 128
units = 256
dropout = 0.2
StopWatch.progress(20)

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
save(model, 'mnist_lstm')

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

StopWatch.stop("compile")
StopWatch.progress(40)


# ## Train



StopWatch.start("train")

model.fit(x_train, y_train, epochs=1, batch_size=batch_size)

StopWatch.stop("train")
StopWatch.progress(80)


# ## Test



StopWatch.start("test")

loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy: %.1f%%" % (100.0 * acc))

StopWatch.stop("test")
StopWatch.stop("total")
StopWatch.progress(100)

if os_is_windows():
    user = os.environ["USERNAME"]
else:
    try:
        user = os.environ['USER']
    except:  # noqa: E722
        user = os.system('basename $HOME')

# try:
#     gpuname = ''
#     for line in open('mlp_mnist.log', 'r'):
#         if 'GPU' in line and line[-2] == ')':
#             gpuname = gpuname + line[:line.find('(')] + '\n'
# except:  # noqa: E722
#     gpuname = cpuinfo.get_cpu_info()['brand_raw']

gpuname = Shell.run('nvidia-smi --list-gpus')

tag = 'mlp_mnist'

StopWatch.benchmark(tag=tag, node=gpuname, user=user)

