# Google Colab Examples

## Distributed Training for MNIST

Distributed Training for MNIST

   
* [Open In Colab](https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mnist_with_distributed_training.ipynb)

* [Open in GitHub) View in Github](https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mnist_with_distributed_training.ipynb)

* [Download](https://raw.githubusercontent.com/cybertraining-dsc/cybertraining-dsc.github.io/master/content/en/modules/notebooks/mnist_with_distributed_training.ipynb)
   

In this lesson we discuss in how to create a simple IPython Notebook to
solve an image classification problem with Multi Layer Perceptron with
LSTM.

### Pre-requisites 

Install the following Python packages

1.  cloudmesh-installer
2.  cloudmesh-common

```
pip3 install cloudmesh-installer
pip3 install cloudmesh-common
```


## Sample MLP + LSTM with Tensorflow Keras 

### Import Libraries 


```
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
```

### Download Data and Pre-Process 


```
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
```

### Define Model 

Here we use the Tensorflow distributed training components to train the
model in multiple CPUs or GPUs. In the Colab instance multiple GPUs are
not supported. Hence, the training must be done in the device type
'None' when selecting the 'runtime type' from Runtime menu. To run with
multiple-GPUs no code change is required. [Learn more about distributed
training](https://www.tensorflow.org/guide/distributed_training).


```
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
```



```
Model: "sequential_2"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
lstm_6 (LSTM)                (None, 28, 256)           291840    
_________________________________________________________________
lstm_7 (LSTM)                (None, 28, 256)           525312    
_________________________________________________________________
lstm_8 (LSTM)                (None, 256)               525312    
_________________________________________________________________
dense_6 (Dense)              (None, 256)               65792     
_________________________________________________________________
activation_6 (Activation)    (None, 256)               0         
_________________________________________________________________
dropout_4 (Dropout)          (None, 256)               0         
_________________________________________________________________
dense_7 (Dense)              (None, 256)               65792     
_________________________________________________________________
activation_7 (Activation)    (None, 256)               0         
_________________________________________________________________
dropout_5 (Dropout)          (None, 256)               0         
_________________________________________________________________
dense_8 (Dense)              (None, 10)                2570      
_________________________________________________________________
activation_8 (Activation)    (None, 10)                0         
=================================================================
Total params: 1,476,618
Trainable params: 1,476,618
Non-trainable params: 0
_________________________________________________________________
INFO:tensorflow:Using MirroredStrategy with devices ('/job:localhost/replica:0/task:0/device:GPU:0',)
Number of devices: 1
INFO:tensorflow:Reduce to /job:localhost/replica:0/task:0/device:CPU:0 then broadcast to ('/job:localhost/replica:0/task:0/device:CPU:0',).
INFO:tensorflow:Reduce to /job:localhost/replica:0/task:0/device:CPU:0 then broadcast to ('/job:localhost/replica:0/task:0/device:CPU:0',).
INFO:tensorflow:Reduce to /job:localhost/replica:0/task:0/device:CPU:0 then broadcast to ('/job:localhost/replica:0/task:0/device:CPU:0',).
INFO:tensorflow:Reduce to /job:localhost/replica:0/task:0/device:CPU:0 then broadcast to ('/job:localhost/replica:0/task:0/device:CPU:0',).
```


### Train 


```
StopWatch.start("train")
model.fit(x_train, y_train, epochs=30, batch_size=batch_size)
StopWatch.stop("train")
```



```
Epoch 1/30
469/469 [==============================] - 7s 16ms/step - loss: 2.0427 - accuracy: 0.2718
Epoch 2/30
469/469 [==============================] - 7s 16ms/step - loss: 1.6934 - accuracy: 0.4007
Epoch 3/30
469/469 [==============================] - 7s 16ms/step - loss: 1.2997 - accuracy: 0.5497
...
Epoch 28/30
469/469 [==============================] - 8s 17ms/step - loss: 0.1175 - accuracy: 0.9640
Epoch 29/30
469/469 [==============================] - 8s 17ms/step - loss: 0.1158 - accuracy: 0.9645
Epoch 30/30
469/469 [==============================] - 8s 17ms/step - loss: 0.1098 - accuracy: 0.9661
```


####Test 


```
StopWatch.start("evaluate")
loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy: %.1f%%" % (100.0 * acc))
StopWatch.stop("evaluate")

StopWatch.benchmark()
```



```
79/79 [==============================] - 3s 9ms/step - loss: 0.0898 - accuracy: 0.9719

Test accuracy: 97.2%

+------------------+----------+---------+---------+---------------------+-------+--------------+--------+-------+-------------------------------------+
| Name             | Status   |    Time |     Sum | Start               | tag   | Node         | User   | OS    | Version                             |
|------------------+----------+---------+---------+---------------------+-------+--------------+--------+-------+-------------------------------------|
| data-load        | failed   |   0.473 |   0.473 | 2021-03-07 11:34:03 |       | b39e0899c1f8 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| data-pre-process | failed   |   0.073 |   0.073 | 2021-03-07 11:34:03 |       | b39e0899c1f8 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| compile          | failed   |   0.876 |   7.187 | 2021-03-07 11:38:05 |       | b39e0899c1f8 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| train            | failed   | 229.341 | 257.023 | 2021-03-07 11:38:44 |       | b39e0899c1f8 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| evaluate         | failed   |   2.659 |   4.25  | 2021-03-07 11:44:54 |       | b39e0899c1f8 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
+------------------+----------+---------+---------+---------------------+-------+--------------+--------+-------+-------------------------------------+
```


### References

1.  [Advance Deep Learning with
    Keras](https://github.com/PacktPublishing/Advanced-Deep-Learning-with-Keras)
2.  [Distributed With
    Tensorflow](https://www.tensorflow.org/guide/distributed_training)
3.  [Keras with Tensorflow Distributed
    Training](https://keras.io/guides/distributed_training/)



## MLP + LSTM with MNIST on Google Colab 


MLP + LSTM with MNIST on Google Colab

* [Open In Colab](https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mnist_mlp_with_lstm.ipynb)

* [Open in GitHub) View in Github](https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mnist_mlp_with_lstm.ipynb)

* [Download](https://raw.githubusercontent.com/cybertraining-dsc/cybertraining-dsc.github.io/master/content/en/modules/notebooks/mnist_mlp_with_lstm.ipynb)


In this lesson we discuss in how to create a simple IPython Notebook to
solve an image classification problem with Multi Layer Perceptron with
LSTM.

### Pre-requisites 

Install the following Python packages

1.  cloudmesh-installer
2.  cloudmesh-common


```
pip3 install cloudmesh-installer
pip3 install cloudmesh-common
```


### Sample MLP + LSTM with Tensorflow Keras 

### Import Libraries 


```
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
```


### Download Data and Pre-Process 


```
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
```


### Define Model 


```
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
```


```
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
lstm (LSTM)                  (None, 28, 256)           291840    
_________________________________________________________________
lstm_1 (LSTM)                (None, 28, 256)           525312    
_________________________________________________________________
lstm_2 (LSTM)                (None, 256)               525312    
_________________________________________________________________
dense (Dense)                (None, 256)               65792     
_________________________________________________________________
activation (Activation)      (None, 256)               0         
_________________________________________________________________
dropout (Dropout)            (None, 256)               0         
_________________________________________________________________
dense_1 (Dense)              (None, 256)               65792     
_________________________________________________________________
activation_1 (Activation)    (None, 256)               0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 256)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 10)                2570      
_________________________________________________________________
activation_2 (Activation)    (None, 10)                0         
=================================================================
Total params: 1,476,618
Trainable params: 1,476,618
Non-trainable params: 0
```

### Train 


```
StopWatch.start("train")
model.fit(x_train, y_train, epochs=30, batch_size=batch_size)
StopWatch.stop("train")
```


```
469/469 [==============================] - 378s 796ms/step - loss: 2.2689 - accuracy: 0.2075
```


### Test 


```
StopWatch.start("evaluate")
loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy: %.1f%%" % (100.0 * acc))
StopWatch.stop("evaluate")

StopWatch.benchmark()
```



```
79/79 [==============================] - 1s 7ms/step - loss: 2.2275 - accuracy: 0.3120

Test accuracy: 31.2%

+------------------+----------+--------+--------+---------------------+-------+--------------+--------+-------+-------------------------------------+
| Name             | Status   |   Time |    Sum | Start               | tag   | Node         | User   | OS    | Version                             |
|------------------+----------+--------+--------+---------------------+-------+--------------+--------+-------+-------------------------------------|
| data-load        | failed   |  0.61  |  0.61  | 2021-02-21 21:35:06 |       | 9810ccb69d08 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| data-pre-process | failed   |  0.076 |  0.076 | 2021-02-21 21:35:07 |       | 9810ccb69d08 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| compile          | failed   |  6.445 |  6.445 | 2021-02-21 21:35:07 |       | 9810ccb69d08 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| train            | failed   | 17.171 | 17.171 | 2021-02-21 21:35:13 |       | 9810ccb69d08 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| evaluate         | failed   |  1.442 |  1.442 | 2021-02-21 21:35:31 |       | 9810ccb69d08 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
+------------------+----------+--------+--------+---------------------+-------+--------------+--------+-------+-------------------------------------+
```


### References

[Orignal Source to Source
Code](https://github.com/PacktPublishing/Advanced-Deep-Learning-with-Keras)

## MNIST Classification on Google Colab 


MNIST Classification on Google Colab

* [Open In Colab](https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/google_colab_mnist_example.ipynb)

* [Open in GitHub) View in Github](https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/google_colab_mnist_example.ipynb)

* [Download](https://raw.githubusercontent.com/cybertraining-dsc/cybertraining-dsc.github.io/master/content/en/modules/notebooks/google_colab_mnist_example.ipynb)


In this lesson we discuss in how to create a simple IPython Notebook to
solve an image classification problem. MNIST contains a set of pictures

### Import Libraries 

Note: <https://python-future.org/quickstart.html>


```
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.utils import to_categorical, plot_model
from keras.datasets import mnist
```

### Warm Up Exercise 

### Pre-process data 

####Load data 

First we load the data from the inbuilt mnist dataset from Keras Here we
have to split the data set into training and testing data. The training
data or testing data has two components. Training features and training
labels. For instance every sample in the dataset has a corresponding
label. In Mnist the training sample contains image data represented in
terms of an array. The training labels are from 0-9.

Here we say x_train for training data features and y_train as the
training labels. Same goes for testing data.


```
(x_train, y_train), (x_test, y_test) = mnist.load_data()
```

    Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz
    11493376/11490434 [==============================] - 0s 0us/step

### Identify Number of Classes 

As this is a number classification problem. We need to know how many
classes are there. So we'll count the number of unique labels.


```
num_labels = len(np.unique(y_train))
```

####Convert Labels To One-Hot Vector 

Read more on one-hot vector.


```
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
```

### Image Reshaping 

The training model is designed by considering the data as a vector. This
is a model dependent modification. Here we assume the image is a squared
shape image.


```
image_size = x_train.shape[1]
input_size = image_size * image_size
```

### Resize and Normalize 

The next step is to continue the reshaping to a fit into a vector and
normalize the data. Image values are from 0 - 255, so an easy way to
normalize is to divide by the maximum value.


```
x_train = np.reshape(x_train, [-1, input_size])
x_train = x_train.astype('float32') / 255
x_test = np.reshape(x_test, [-1, input_size])
x_test = x_test.astype('float32') / 255
```

### Create a Keras Model 

Keras is a neural network library. The summary function provides tabular
summary on the model you created. And the plot_model function provides a
grpah on the network you created.


```
# Create Model
# network parameters
batch_size = 4
hidden_units = 64

model = Sequential()
model.add(Dense(hidden_units, input_dim=input_size))
model.add(Dense(num_labels))
model.add(Activation('softmax'))
model.summary()
plot_model(model, to_file='mlp-mnist.png', show_shapes=True)
```

    Model: "sequential_1"
    _________________________________________________________________
    Layer (type)                 Output Shape              Param #   
    =================================================================
    dense_5 (Dense)              (None, 512)               401920    
    _________________________________________________________________
    dense_6 (Dense)              (None, 10)                5130      
    _________________________________________________________________
    activation_5 (Activation)    (None, 10)                0         
    =================================================================
    Total params: 407,050
    Trainable params: 407,050
    Non-trainable params: 0
    _________________________________________________________________

![images](nnn_files/output_20_1.png)



### Compile and Train 

A keras model need to be compiled before it can be used to train the
model. In the compile function, you can provide the optimization that
you want to add, metrics you expect and the type of loss function you
need to use.

Here we use adam optimizer, a famous optimizer used in neural networks.

The loss funtion we have used is the categorical_crossentropy.

Once the model is compiled, then the fit function is called upon passing
the number of epochs, traing data and batch size.

The batch size determines the number of elements used per minibatch in
optimizing the function.

**Note: Change the number of epochs, batch size and see what happens.**


```
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=1, batch_size=batch_size)
```

    469/469 [==============================] - 3s 7ms/step - loss: 0.3647 - accuracy: 0.8947





    <tensorflow.python.keras.callbacks.History at 0x7fe88faf4c50>

### Testing 

Now we can test the trained model. Use the evaluate function by passing
test data and batch size and the accuracy and the loss value can be
retrieved.

**MNIST_V1.0\|Exercise: Try to observe the network behavior by changing
the number of epochs, batch size and record the best accuracy that you
can gain. Here you can record what happens when you change these values.
Describe your observations in 50-100 words.**


```
loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy: %.1f%%" % (100.0 * acc))
```

    79/79 [==============================] - 0s 4ms/step - loss: 0.2984 - accuracy: 0.9148

    Test accuracy: 91.5%

### Final Note 

This programme can be defined as a hello world programme in deep
learning. Objective of this exercise is not to teach you the depths of
deep learning. But to teach you basic concepts that may need to design a
simple network to solve a problem. Before running the whole code, read
all the instructions before a code section.

### Assignments

1. Solve Exercise MNIST_V1.0.

### References

[Orignal Source to Source
Code](https://github.com/PacktPublishing/Advanced-Deep-Learning-with-Keras)

## MNIST With PyTorch 

MNIST With PyTorch

* [Open In Colab](https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mnist_with_pytorch.ipynb)

* [Open in GitHub) View in Github](https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mnist_with_pytorch.ipynb)

* [Download](https://raw.githubusercontent.com/cybertraining-dsc/cybertraining-dsc.github.io/master/content/en/modules/notebooks/mnist_with_pytorch.ipynb)


In this lesson we discuss in how to create a simple IPython Notebook to
solve an image classification problem with Multi Layer Perceptron with
PyTorch.

### Import Libraries 


```
import numpy as np
import torch
import torchvision
import matplotlib.pyplot as plt
from torchvision import datasets, transforms
from torch import nn
from torch import optim
from time import time
import os
from google.colab import drive
```


### Pre-Process Data 

Here we download the data using PyTorch data utils and transform the
data by using a normalization function. PyTorch provides a data loader
abstraction called a `DataLoader` where we can set the batch size, data
shuffle per batch loading. Each data loader expecte a Pytorch Dataset.
The DataSet abstraction and DataLoader usage can be found
[here](https://pytorch.org/tutorials/recipes/recipes/loading_data_recipe.html)


```
# Data transformation function 
transform = transforms.Compose([transforms.ToTensor(),
                              transforms.Normalize((0.5,), (0.5,)),
                              ])

# DataSet
train_data_set = datasets.MNIST('drive/My Drive/mnist/data/', download=True, train=True, transform=transform)
validation_data_set = datasets.MNIST('drive/My Drive/mnist/data/', download=True, train=False, transform=transform)

# DataLoader
train_loader = torch.utils.data.DataLoader(train_data_set, batch_size=32, shuffle=True)
validation_loader = torch.utils.data.DataLoader(validation_data_set, batch_size=32, shuffle=True)
```


### Define Network 

Here we select the matching input size compared to the network
definition. Here data reshaping or layer reshaping must be done to match
input data shape with the network input shape. Also we define a set of
hidden unit sizes along with the output layers size. The `output_size`
must match with the number of labels associated with the classification
problem. The hidden units can be chosesn depending on the problem.
`nn.Sequential` is one way to create the network. Here we stack a set of
linear layers along with a softmax layer for the classification as the
output layer.


```
input_size = 784
hidden_sizes = [128, 128, 64, 64]
output_size = 10

model = nn.Sequential(nn.Linear(input_size, hidden_sizes[0]),
                      nn.ReLU(),
                      nn.Linear(hidden_sizes[0], hidden_sizes[1]),
                      nn.ReLU(),
                      nn.Linear(hidden_sizes[1], hidden_sizes[2]),
                      nn.ReLU(),
                      nn.Linear(hidden_sizes[2], hidden_sizes[3]),
                      nn.ReLU(),
                      nn.Linear(hidden_sizes[3], output_size),
                      nn.LogSoftmax(dim=1))

                      
print(model)
```



```
Sequential(
  (0): Linear(in_features=784, out_features=128, bias=True)
  (1): ReLU()
  (2): Linear(in_features=128, out_features=128, bias=True)
  (3): ReLU()
  (4): Linear(in_features=128, out_features=64, bias=True)
  (5): ReLU()
  (6): Linear(in_features=64, out_features=64, bias=True)
  (7): ReLU()
  (8): Linear(in_features=64, out_features=10, bias=True)
  (9): LogSoftmax(dim=1)
)
```


### Define Loss Function and Optimizer 

Read more about [Loss
Functions](https://pytorch.org/docs/stable/nn.html#loss-functions) and
[Optimizers](https://pytorch.org/docs/stable/optim.html) supported by
PyTorch.


```
criterion = nn.NLLLoss()
optimizer = optim.SGD(model.parameters(), lr=0.003, momentum=0.9)
```


### Train 


```
epochs = 5

for epoch in range(epochs):
    loss_per_epoch = 0
    for images, labels in train_loader:
        images = images.view(images.shape[0], -1)
    
        # Gradients cleared per batch
        optimizer.zero_grad()
        
        # Pass input to the model
        output = model(images)
        # Calculate loss after training compared to labels
        loss = criterion(output, labels)
        
        # backpropagation 
        loss.backward()
        
        # optimizer step to update the weights
        optimizer.step()
        
        loss_per_epoch += loss.item()
    average_loss = loss_per_epoch / len(train_loader)
    print("Epoch {} - Training loss: {}".format(epoch, average_loss))
```



```
Epoch 0 - Training loss: 1.3052690227402808
Epoch 1 - Training loss: 0.33809808635317695
Epoch 2 - Training loss: 0.22927882223685922
Epoch 3 - Training loss: 0.16807103878669521
Epoch 4 - Training loss: 0.1369301250545995
```


### Model Evaluation 

Similar to training data loader, we use the validation loader to load
batch by batch and run the feed-forward network to get the expected
prediction and compared to the label associated with the data point.


```
correct_predictions, all_count = 0, 0
# enumerate data from the data validation loader (loads a batch at a time)
for batch_id, (images,labels) in enumerate(validation_loader):
  for i in range(len(labels)):
    img = images[i].view(1, 784)
    # at prediction stage, only feed-forward calculation is required. 
    with torch.no_grad():
        logps = model(img)

    # Output layer of the network uses a LogSoftMax layer
    # Hence the probability must be calculated with the exponential values. 
    # The final layer returns an array of probabilities for each label
    # Pick the maximum probability and the corresponding index
    # The corresponding index is the predicted label 
    ps = torch.exp(logps)
    probab = list(ps.numpy()[0])
    pred_label = probab.index(max(probab))
    true_label = labels.numpy()[i]
    if(true_label == pred_label):
      correct_predictions += 1
    all_count += 1

print(f"Model Accuracy {(correct_predictions/all_count) * 100} %")
```



```
Model Accuracy 95.95 %
```


### References 

1.  [Torch NN
    Sequential](https://pytorch.org/docs/stable/generated/torch.nn.Sequential.html)
2.  [Handwritten Digit Recognition Using PyTorch --- Intro To Neural
    Networks](https://towardsdatascience.com/handwritten-digit-mnist-pytorch-977b5338e627)
3.  [MNIST Handwritten Digit Recognition in
    PyTorch](https://nextjournal.com/gkoehler/pytorch-mnist)



## MNIST-AutoEncoder Classification on Google Colab 


MNIST with AutoEncoder: Classification on Google Colab

* [Open In Colab](https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mnist_autoencoder.ipynb)

* [Open in GitHub) View in Github](https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mnist_autoencoder.ipynb)

* [Download](https://raw.githubusercontent.com/cybertraining-dsc/cybertraining-dsc.github.io/master/content/en/modules/notebooks/mnist_autoencoder.ipynb)


### Prerequisites 

Install the following packages


```
! pip3 install cloudmesh-installer
! pip3 install cloudmesh-common
```


### Import Libraries 


```
import tensorflow as tf
from keras.layers import Dense, Input
from keras.layers import Conv2D, Flatten
from keras.layers import Reshape, Conv2DTranspose
from keras.models import Model
from keras.datasets import mnist
from keras.utils import plot_model
from keras import backend as K

import numpy as np
import matplotlib.pyplot as plt
```


### Download Data and Pre-Process 


```
(x_train, y_train), (x_test, y_test) = mnist.load_data()

image_size = x_train.shape[1]
x_train = np.reshape(x_train, [-1, image_size, image_size, 1])
x_test = np.reshape(x_test, [-1, image_size, image_size, 1])
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

input_shape = (image_size, image_size, 1)
batch_size = 32
kernel_size = 3
latent_dim = 16
hidden_units = [32, 64]
```


```
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz
11493376/11490434 [==============================] - 0s 0us/step
```


### Define Model 


```
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
plot_model(encoder,
           to_file='encoder.png',
           show_shapes=True)


latent_inputs = Input(shape=(latent_dim,), name='decoder_input')
x = Dense(shape[1] * shape[2] * shape[3])(latent_inputs)
x = Reshape((shape[1], shape[2], shape[3]))(x)
x = Dense(hidden_units[0], activation='relu')(x)
x = Dense(hidden_units[1], activation='relu')(x)

outputs = Dense(1, activation='relu')(x)

decoder = Model(latent_inputs, outputs, name='decoder')
decoder.summary()
plot_model(decoder, to_file='decoder.png', show_shapes=True)

autoencoder = Model(inputs,
                    decoder(encoder(inputs)),
                    name='autoencoder')
autoencoder.summary()
plot_model(autoencoder,
           to_file='autoencoder.png',
           show_shapes=True)

autoencoder.compile(loss='mse', optimizer='adam')
```



```
Model: "encoder"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
encoder_input (InputLayer)   [(None, 28, 28, 1)]       0         
_________________________________________________________________
dense_2 (Dense)              (None, 28, 28, 32)        64        
_________________________________________________________________
dense_3 (Dense)              (None, 28, 28, 64)        2112      
_________________________________________________________________
flatten_1 (Flatten)          (None, 50176)             0         
_________________________________________________________________
latent_vector (Dense)        (None, 16)                802832    
=================================================================
Total params: 805,008
Trainable params: 805,008
Non-trainable params: 0
_________________________________________________________________
Model: "decoder"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
decoder_input (InputLayer)   [(None, 16)]              0         
_________________________________________________________________
dense_4 (Dense)              (None, 50176)             852992    
_________________________________________________________________
reshape (Reshape)            (None, 28, 28, 64)        0         
_________________________________________________________________
dense_5 (Dense)              (None, 28, 28, 32)        2080      
_________________________________________________________________
dense_6 (Dense)              (None, 28, 28, 64)        2112      
_________________________________________________________________
dense_7 (Dense)              (None, 28, 28, 1)         65        
=================================================================
Total params: 857,249
Trainable params: 857,249
Non-trainable params: 0
_________________________________________________________________
Model: "autoencoder"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
encoder_input (InputLayer)   [(None, 28, 28, 1)]       0         
_________________________________________________________________
encoder (Functional)         (None, 16)                805008    
_________________________________________________________________
decoder (Functional)         (None, 28, 28, 1)         857249    
=================================================================
Total params: 1,662,257
Trainable params: 1,662,257
Non-trainable params: 0
```


### Train 


```
autoencoder.fit(x_train,
                x_train,
                validation_data=(x_test, x_test),
                epochs=1,
                batch_size=batch_size)
```



```
1875/1875 [==============================] - 112s 60ms/step - loss: 0.0268 - val_loss: 0.0131

<tensorflow.python.keras.callbacks.History at 0x7f3ecb2e0be0>
```


### Test 


```
x_decoded = autoencoder.predict(x_test)
```



```
79/79 [==============================] - 7s 80ms/step - loss: 0.2581 - accuracy: 0.9181

Test accuracy: 91.8%
```


### Visualize 


```
imgs = np.concatenate([x_test[:8], x_decoded[:8]])
imgs = imgs.reshape((4, 4, image_size, image_size))
imgs = np.vstack([np.hstack(i) for i in imgs])
plt.figure()
plt.axis('off')
plt.title('Input: 1st 2 rows, Decoded: last 2 rows')
plt.imshow(imgs, interpolation='none', cmap='gray')
plt.savefig('input_and_decoded.png')
plt.show()
```



## MNIST-CNN Classification on Google Colab 


MNIST with Convolutional Neural Networks: Classification on Google Colab



* [Open In Colab](https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mnist_cnn.ipynb)

* [Open in GitHub) View in Github](https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mnist_cnn.ipynb)

* [Download](https://raw.githubusercontent.com/cybertraining-dsc/cybertraining-dsc.github.io/master/content/en/modules/notebooks/mnist_cnn.ipynb)


### Prerequisites 

Install the following packages


```
! pip3 install cloudmesh-installer
! pip3 install cloudmesh-common
```


### Import Libraries 


```
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout
from keras.layers import Conv2D, MaxPooling2D, Flatten, AveragePooling2D
from keras.utils import to_categorical, plot_model
from keras.datasets import mnist
```


### Download Data and Pre-Process 


```
(x_train, y_train), (x_test, y_test) = mnist.load_data()

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
```



```
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz
11493376/11490434 [==============================] - 0s 0us/step
(28, 28, 1)
```


### Define Model 


```
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
```



```
Model: "sequential_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_4 (Conv2D)            (None, 28, 28, 64)        640       
_________________________________________________________________
max_pooling2d_3 (MaxPooling2 (None, 14, 14, 64)        0         
_________________________________________________________________
conv2d_5 (Conv2D)            (None, 14, 14, 64)        36928     
_________________________________________________________________
max_pooling2d_4 (MaxPooling2 (None, 7, 7, 64)          0         
_________________________________________________________________
conv2d_6 (Conv2D)            (None, 7, 7, 64)          36928     
_________________________________________________________________
max_pooling2d_5 (MaxPooling2 (None, 3, 3, 64)          0         
_________________________________________________________________
conv2d_7 (Conv2D)            (None, 1, 1, 64)          36928     
_________________________________________________________________
flatten_1 (Flatten)          (None, 64)                0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 64)                0         
_________________________________________________________________
dense_1 (Dense)              (None, 10)                650       
_________________________________________________________________
activation_1 (Activation)    (None, 10)                0         
=================================================================
Total params: 112,074
Trainable params: 112,074
Non-trainable params: 0
_________________________________________________________________
```


### Train 


```
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
# train the network
model.fit(x_train, y_train, epochs=10, batch_size=batch_size)
```



```
469/469 [==============================] - 125s 266ms/step - loss: 0.6794 - accuracy: 0.7783

<tensorflow.python.keras.callbacks.History at 0x7f35d4b104e0>
```


### Test 


```
loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy: %.1f%%" % (100.0 * acc))
```



```
79/79 [==============================] - 6s 68ms/step - loss: 0.0608 - accuracy: 0.9813

Test accuracy: 98.1%
```




## MNIST-LSTM Classification on Google Colab 


MNIST-LSTM Classification on Google Colab

* [Open In Colab](https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mnist_lstm.ipynb)

* [Open in GitHub) View in Github](https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mnist_lstm.ipynb)

* [Download](https://raw.githubusercontent.com/cybertraining-dsc/cybertraining-dsc.github.io/master/content/en/modules/notebooks/mnist_lstm.ipynb)


### Pre-requisites 

Install the following Python packages

1.  cloudmesh-installer
2.  cloudmesh-common


```
pip3 install cloudmesh-installer
pip3 install cloudmesh-common
```


### Sample LSTM with Tensorflow Keras 

### Import Libraries 


```
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, SimpleRNN, InputLayer, LSTM
from tensorflow.keras.utils import to_categorical, plot_model
from tensorflow.keras.datasets import mnist
from cloudmesh.common.StopWatch import StopWatch
```


### Download Data and Pre-Process 


```
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
```


### Define Model 


```
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


model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
StopWatch.stop("compile")
```



```
Model: "sequential_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
lstm_3 (LSTM)                (None, 28, 256)           291840    
_________________________________________________________________
lstm_4 (LSTM)                (None, 28, 256)           525312    
_________________________________________________________________
lstm_5 (LSTM)                (None, 256)               525312    
_________________________________________________________________
dense_1 (Dense)              (None, 10)                2570      
_________________________________________________________________
activation_1 (Activation)    (None, 10)                0         
=================================================================
Total params: 1,345,034
Trainable params: 1,345,034
Non-trainable params: 0
```


### Train 


```
StopWatch.start("train")
model.fit(x_train, y_train, epochs=1, batch_size=batch_size)
StopWatch.stop("train")
```



```
469/469 [==============================] - 378s 796ms/step - loss: 2.2689 - accuracy: 0.2075
```


### Test 


```
StopWatch.start("evaluate")
loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy: %.1f%%" % (100.0 * acc))
StopWatch.stop("evaluate")

StopWatch.benchmark()
```



```
79/79 [==============================] - 22s 260ms/step - loss: 1.9646 - accuracy: 0.3505

Test accuracy: 35.0%

+------------------+----------+---------+---------+---------------------+-------+--------------+--------+-------+-------------------------------------+
| Name             | Status   |    Time |     Sum | Start               | tag   | Node         | User   | OS    | Version                             |
|------------------+----------+---------+---------+---------------------+-------+--------------+--------+-------+-------------------------------------|
| data-load        | failed   |   0.354 |   0.967 | 2021-02-18 15:27:21 |       | 351ef0f61c92 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| data-pre-process | failed   |   0.098 |   0.198 | 2021-02-18 15:27:21 |       | 351ef0f61c92 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| compile          | failed   |   0.932 |   2.352 | 2021-02-18 15:27:23 |       | 351ef0f61c92 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| train            | failed   | 377.842 | 377.842 | 2021-02-18 15:27:26 |       | 351ef0f61c92 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| evaluate         | failed   |  21.689 |  21.689 | 2021-02-18 15:33:44 |       | 351ef0f61c92 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
+------------------+----------+---------+---------+---------------------+-------+--------------+--------+-------+-------------------------------------+
```


### References 

[Orignal Source to Source
Code](https://github.com/PacktPublishing/Advanced-Deep-Learning-with-Keras)



## MNIST-MLP Classification on Google Colab 


MNIST-MLP Classification on Google Colab


* [Open In Colab](https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mlp_mnist.ipynb)

* [Open in GitHub) View in Github](https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mlp_mnist.ipynb)

* [Download](https://raw.githubusercontent.com/cybertraining-dsc/cybertraining-dsc.github.io/master/content/en/modules/notebooks/mlp_mnist.ipynb)


In this lesson we discuss in how to create a simple IPython Notebook to
solve an image classification problem with Multi Layer Perceptron.

### Pre-requisites 

Install the following Python packages

1.  cloudmesh-installer
2.  cloudmesh-common


```
pip3 install cloudmesh-installer
pip3 install cloudmesh-common
```


### Sample MLP with Tensorflow Keras 


```
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import time 

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.utils import to_categorical, plot_model
from keras.datasets import mnist
#import pydotplus
from keras.utils.vis_utils import model_to_dot
#from keras.utils.vis_utils import pydot


from cloudmesh.common.StopWatch import StopWatch

StopWatch.start("data-load")
(x_train, y_train), (x_test, y_test) = mnist.load_data()
StopWatch.stop("data-load")

num_labels = len(np.unique(y_train))


y_train = to_categorical(y_train)
y_test = to_categorical(y_test)


image_size = x_train.shape[1]
input_size = image_size * image_size


x_train = np.reshape(x_train, [-1, input_size])
x_train = x_train.astype('float32') / 255
x_test = np.reshape(x_test, [-1, input_size])
x_test = x_test.astype('float32') / 255

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
plot_model(model, to_file='mlp-mnist.png', show_shapes=True)

StopWatch.start("compile")
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
StopWatch.stop("compile")
StopWatch.start("train")
model.fit(x_train, y_train, epochs=5, batch_size=batch_size)
StopWatch.stop("train")

StopWatch.start("test")
loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy: %.1f%%" % (100.0 * acc))
StopWatch.stop("test")

StopWatch.benchmark()
```



```
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz
11493376/11490434 [==============================] - 0s 0us/step
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense (Dense)                (None, 512)               401920    
_________________________________________________________________
activation (Activation)      (None, 512)               0         
_________________________________________________________________
dropout (Dropout)            (None, 512)               0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               262656    
_________________________________________________________________
activation_1 (Activation)    (None, 512)               0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 512)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 512)               262656    
_________________________________________________________________
activation_2 (Activation)    (None, 512)               0         
_________________________________________________________________
dropout_2 (Dropout)          (None, 512)               0         
_________________________________________________________________
dense_3 (Dense)              (None, 512)               262656    
_________________________________________________________________
activation_3 (Activation)    (None, 512)               0         
_________________________________________________________________
dropout_3 (Dropout)          (None, 512)               0         
_________________________________________________________________
dense_4 (Dense)              (None, 10)                5130      
_________________________________________________________________
activation_4 (Activation)    (None, 10)                0         
=================================================================
Total params: 1,195,018
Trainable params: 1,195,018
Non-trainable params: 0
_________________________________________________________________
Epoch 1/5
469/469 [==============================] - 14s 29ms/step - loss: 0.7886 - accuracy: 0.7334
Epoch 2/5
469/469 [==============================] - 14s 29ms/step - loss: 0.1981 - accuracy: 0.9433
Epoch 3/5
469/469 [==============================] - 14s 29ms/step - loss: 0.1546 - accuracy: 0.9572
Epoch 4/5
469/469 [==============================] - 14s 29ms/step - loss: 0.1302 - accuracy: 0.9641
Epoch 5/5
469/469 [==============================] - 14s 29ms/step - loss: 0.1168 - accuracy: 0.9663
79/79 [==============================] - 1s 9ms/step - loss: 0.0785 - accuracy: 0.9765

Test accuracy: 97.6%

+-----------+----------+--------+--------+---------------------+-------+--------------+--------+-------+-------------------------------------+
| Name      | Status   |   Time |    Sum | Start               | tag   | Node         | User   | OS    | Version                             |
|-----------+----------+--------+--------+---------------------+-------+--------------+--------+-------+-------------------------------------|
| data-load | failed   |  0.549 |  0.549 | 2021-02-15 15:24:00 |       | 6609095905d1 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| compile   | failed   |  0.023 |  0.023 | 2021-02-15 15:24:01 |       | 6609095905d1 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| train     | failed   | 69.1   | 69.1   | 2021-02-15 15:24:01 |       | 6609095905d1 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| test      | failed   |  0.907 |  0.907 | 2021-02-15 15:25:10 |       | 6609095905d1 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
+-----------+----------+--------+--------+---------------------+-------+--------------+--------+-------+-------------------------------------+
```


### References

[Orignal Source to Source
Code](https://github.com/PacktPublishing/Advanced-Deep-Learning-with-Keras)



## MNIST-RMM Classification on Google Colab 


MNIST with Recurrent Neural Networks: Classification on Google Colab



* [Open In Colab](https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mnist_rnn.ipynb)

* [Open in GitHub) View in Github](https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/mnist_rnn.ipynb)

* [Download](https://raw.githubusercontent.com/cybertraining-dsc/cybertraining-dsc.github.io/master/content/en/modules/notebooks/mnist_rnn.ipynb)



### Prerequisites 

Install the following packages


```
! pip3 install cloudmesh-installer
! pip3 install cloudmesh-common
```


### Import Libraries 


```
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, SimpleRNN
from tensorflow.keras.utils import to_categorical, plot_model
from tensorflow.keras.datasets import mnist
from cloudmesh.common.StopWatch import StopWatch
```


### Download Data and Pre-Process 


```
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
```


### Define Model 


```
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
```



```
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
simple_rnn (SimpleRNN)       (None, 28, 256)           72960     
_________________________________________________________________
simple_rnn_1 (SimpleRNN)     (None, 28, 256)           131328    
_________________________________________________________________
simple_rnn_2 (SimpleRNN)     (None, 256)               131328    
_________________________________________________________________
dense (Dense)                (None, 10)                2570      
_________________________________________________________________
activation (Activation)      (None, 10)                0         
=================================================================
Total params: 338,186
Trainable params: 338,186
Non-trainable params: 0
```


### Train 


```
StopWatch.start("train")
model.fit(x_train, y_train, epochs=1, batch_size=batch_size)
StopWatch.stop("train")
```



```
469/469 [==============================] - 125s 266ms/step - loss: 0.6794 - accuracy: 0.7783

<tensorflow.python.keras.callbacks.History at 0x7f35d4b104e0>
```


### Test 


```
StopWatch.start("evaluate")
loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy: %.1f%%" % (100.0 * acc))
StopWatch.stop("evaluate")

StopWatch.benchmark()
```



```
79/79 [==============================] - 7s 80ms/step - loss: 0.2581 - accuracy: 0.9181

Test accuracy: 91.8%

+------------------+----------+---------+---------+---------------------+-------+--------------+--------+-------+-------------------------------------+
| Name             | Status   |    Time |     Sum | Start               | tag   | Node         | User   | OS    | Version                             |
|------------------+----------+---------+---------+---------------------+-------+--------------+--------+-------+-------------------------------------|
| data-load        | failed   |   0.36  |   0.36  | 2021-02-18 15:16:12 |       | 8f16b3b1f784 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| data-pre-process | failed   |   0.086 |   0.086 | 2021-02-18 15:16:12 |       | 8f16b3b1f784 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| compile          | failed   |   0.51  |   0.51  | 2021-02-18 15:16:12 |       | 8f16b3b1f784 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| train            | failed   | 126.612 | 126.612 | 2021-02-18 15:16:13 |       | 8f16b3b1f784 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| evaluate         | failed   |   6.798 |   6.798 | 2021-02-18 15:18:19 |       | 8f16b3b1f784 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
+------------------+----------+---------+---------+---------------------+-------+--------------+--------+-------+-------------------------------------+
```


### References

[Orignal Source to Source
Code](https://github.com/PacktPublishing/Advanced-Deep-Learning-with-Keras)





