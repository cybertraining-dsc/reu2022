#!/usr/bin/env python
# coding: utf-8

# # MNIST with Recurrent Neural Networks
# This program runs in about 46.033 seconds (Windows 11, i7, 16 GB)

# ## Pre-requisites
# 
# Install the following Python packages
# 
# 1. cloudmesh-installer
# 2. cloudmesh-common



from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.Shell import Shell    # noqa: E402
from cloudmesh.common.variables import Variables
from cloudmesh.common.StopWatch import progress

gpuname = Shell.run('nvidia-smi --list-gpus')
v = Variables()
gpuname = v['currentgpu']
filename = Shell.map_filename(f'~/reu2022/code/deeplearning/mnist/mnist_rnn-{gpuname}.log').path


# ## Exporting Output Graphs



def save(graph, filename):
    if os.path.exists("images"):
        pass
    else:
        Shell.mkdir("images")
    plot_model(graph, to_file=f'images/{filename}.png', show_shapes=True)
    plot_model(graph, to_file=f'images/{filename}.pdf', show_shapes=True)


# ## Import Libraries



StopWatch.start("total")
StopWatch.start("import")
progress(progress=0, filename=filename)

import os    # noqa: E402
import cpuinfo    # noqa: E402
import numpy as np    # noqa: E402
from keras.models import Sequential    # noqa: E402
from keras.layers import Dense, Activation, SimpleRNN    # noqa: E402
from keras.utils import to_categorical, plot_model    # noqa: E402
from keras.datasets import mnist    # noqa: E402
from cloudmesh.common.systeminfo import os_is_windows    # noqa: E402

StopWatch.stop("import")
progress(progress=5, filename=filename)


# ## Data Load



StopWatch.start("data-load")

(x_train, y_train), (x_test, y_test) = mnist.load_data()

StopWatch.stop("data-load")
progress(progress=6, filename=filename)


# ## Data Pre-Process



StopWatch.start("data-pre-process")

num_labels = len(np.unique(y_train))

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

image_size = x_train.shape[1]
x_train = np.reshape(x_train, [-1, image_size, image_size])
x_test = np.reshape(x_test, [-1, image_size, image_size])
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

StopWatch.stop("data-pre-process")
progress(progress=7, filename=filename)


# ## Define Model



StopWatch.start("compile")

input_shape = (image_size, image_size)
batch_size = 128
units = 256
dropout = 0.2

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
save(model, 'mnist_rnn')

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

StopWatch.stop("compile")
progress(progress=8, filename=filename)


# ## Train



StopWatch.start("train")

model.fit(x_train, y_train, epochs=1, batch_size=batch_size)

StopWatch.stop("train")
progress(progress=95, filename=filename)


# ## Test



StopWatch.start("evaluate")

loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy: %.1f%%" % (100.0 * acc))

StopWatch.stop("evaluate")
StopWatch.stop("total")
progress(progress=100, filename=filename)

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


tag = 'mlp_mnist'

StopWatch.benchmark(tag=tag, node=gpuname, user=user, filename=filename)

