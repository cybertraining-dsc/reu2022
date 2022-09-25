#!/usr/bin/env python
# coding: utf-8

# # MNIST Auto-Encoder
# 
# This program runs in about 67.565 seconds (Windows 11, Intel i7, 16 GB)

# ## Pre-requisites
# 
# Install the following Python packages
# 
# 1. cloudmesh-installer
# 2. cloudmesh-common

import os


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



StopWatch.start("total")
StopWatch.start("import")
StopWatch.progress(0)

import os    # noqa: E402
import cpuinfo    # noqa: E402
import numpy as np    # noqa: E402
import matplotlib.pyplot as plt    # noqa: E402
from keras.layers import Dense, Input    # noqa: E402
from keras.layers import Conv2D, Flatten    # noqa: E402
from keras.layers import Reshape, Conv2DTranspose    # noqa: E402
from keras.models import Model    # noqa: E402
from keras.datasets import mnist    # noqa: E402
from keras.utils import plot_model    # noqa: E402
from keras import backend as K    # noqa: E402
from cloudmesh.common.systeminfo import os_is_windows    # noqa: E402
from cloudmesh.common.Shell import Shell    # noqa: E402

StopWatch.stop("import")
StopWatch.progress(10)


# ## Data Load



StopWatch.start("data-load")

(x_train, y_train), (x_test, y_test) = mnist.load_data()

StopWatch.stop("data-load")
StopWatch.progress(11)


# ## Data Pre-Process



StopWatch.start("data-pre-process")

image_size = x_train.shape[1]
x_train = np.reshape(x_train, [-1, image_size, image_size, 1])
x_test = np.reshape(x_test, [-1, image_size, image_size, 1])
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

input_shape = (image_size, image_size, 1)

StopWatch.stop("data-pre-process")
StopWatch.progress(12)


# ## Define Model



StopWatch.start("compile")

batch_size = 32
kernel_size = 3
latent_dim = 16
hidden_units = [32, 64]

inputs = Input(shape=input_shape, name='encoder_input')
x = inputs
x = Dense(hidden_units[0], activation='relu')(x)
x = Dense(hidden_units[1], activation='relu')(x)

shape = K.int_shape(x)

# generate latent vector
x = Flatten()(x)
latent = Dense(latent_dim, name='latent_vector')(x)

# instantiate encoder model
encoder = Model(inputs,
                latent,
                name='encoder')
encoder.summary()
save(encoder, 'encoder')

latent_inputs = Input(shape=(latent_dim,), name='decoder_input')
x = Dense(shape[1] * shape[2] * shape[3])(latent_inputs)
x = Reshape((shape[1], shape[2], shape[3]))(x)
x = Dense(hidden_units[0], activation='relu')(x)
x = Dense(hidden_units[1], activation='relu')(x)

outputs = Dense(1, activation='relu')(x)

decoder = Model(latent_inputs, outputs, name='decoder')
decoder.summary()
save(decoder, 'decoder')

autoencoder = Model(inputs,
                    decoder(encoder(inputs)),
                    name='autoencoder')
autoencoder.summary()
save(autoencoder, 'autoencoder')

autoencoder.compile(loss='mse', optimizer='adam')

StopWatch.stop('compile')
StopWatch.progress(15)


# ## Train



StopWatch.start("train")

autoencoder.fit(x_train,
                x_train,
                validation_data=(x_test, x_test),
                epochs=1,
                batch_size=batch_size)

StopWatch.stop("train")
StopWatch.progress(95)


# ## Test



StopWatch.start("test")

x_decoded = autoencoder.predict(x_test)

StopWatch.stop("test")
StopWatch.progress(99)


# ## Visualize



StopWatch.start("visualize")

imgs = np.concatenate([x_test[:8], x_decoded[:8]])
imgs = imgs.reshape((4, 4, image_size, image_size))
imgs = np.vstack([np.hstack(i) for i in imgs])
plt.figure()
plt.axis('off')
plt.title('Input: 1st 2 rows, Decoded: last 2 rows')
plt.imshow(imgs, interpolation='none', cmap='gray')
plt.savefig(f'images/input_and_decoded.png',dpi=300)
plt.savefig(f'images/input_and_decoded.pdf')
plt.savefig(f'images/input_and_decoded.svg')

StopWatch.stop("visualize")
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
#     for line in open('mnist_autoencoder.log', 'r'):
#         if 'GPU' in line and line[-2] == ')':
#             gpuname = gpuname + line[:line.find('(')] + '\n'
# except:  # noqa: E722
#     gpuname = cpuinfo.get_cpu_info()['brand_raw']

gpuname = Shell.run('nvidia-smi --list-gpus')

tag = 'mnist_autoencoder'

StopWatch.benchmark(tag=tag, node=gpuname, user=user)

