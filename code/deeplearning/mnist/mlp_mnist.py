#!/usr/bin/env python
# coding: utf-8

# # Multi-Layer Perceptron with MNIST
# 
# 
# This program runs in about 29.620 seconds (Windows 11, Intel i7, 16 GB)

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


# ## Exporting Output Graphs



def save(graph, filename):
    if os.path.exists("images"):
        pass
    else:
        Shell.mkdir("images")
    plot_model(graph, to_file=f'images/{filename}.png', show_shapes=True)
    plot_model(graph, to_file=f'images/{filename}.pdf', show_shapes=True)


# ## Import Libraries

gpuname = Shell.run('nvidia-smi --list-gpus')
v = Variables()
gpuname = v['currentgpu']

StopWatch.start("total")
StopWatch.start("import")
filename = Shell.map_filename(f'~/reu2022/code/deeplearning/mnist/mlp_mnist-{gpuname}.log').path
print(filename)
Shell.rm(filename)
progress(progress=0, filename=filename)

import os    # noqa: E402
import cpuinfo  #noqa: E402
import numpy as np    # noqa: E402
from keras.models import Sequential    # noqa: E402
from keras.layers import Dense, Activation, Dropout    # noqa: E402
from keras.utils import to_categorical, plot_model    # noqa: E402
from keras.datasets import mnist    # noqa: E402
from cloudmesh.common.systeminfo import os_is_windows    # noqa: E402

StopWatch.stop("import")
progress(progress=10, filename=filename)


# ## Data Load



StopWatch.start("data-load")

(x_train, y_train), (x_test, y_test) = mnist.load_data()

StopWatch.stop("data-load")
progress(progress=11, filename=filename)


# ## Data Pre-Process



StopWatch.start("data-pre-process")

num_labels = len(np.unique(y_train))

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

image_size = x_train.shape[1]
input_size = image_size * image_size

x_train = np.reshape(x_train, [-1, input_size])
x_train = x_train.astype('float32') / 255
x_test = np.reshape(x_test, [-1, input_size])
x_test = x_test.astype('float32') / 255

StopWatch.stop("data-pre-process")
progress(progress=12, filename=filename)


# ## Define Model



StopWatch.start("compile")

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
save(model, 'mlp_mnist')

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

StopWatch.stop("compile")
progress(progress=13, filename=filename)


# ## Train



StopWatch.start("train")

model.fit(x_train, y_train, epochs=5, batch_size=batch_size)

StopWatch.stop("train")
progress(progress=98, filename=filename)


# ## Test



StopWatch.start("test")

loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy: %.1f%%" % (100.0 * acc))

StopWatch.stop("test")
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


# # REFERENCES
# 
# 1. [Adavnced Keras Deep Learning Book](https://github.com/PacktPublishing/Advanced-Deep-Learning-with-Keras)
