#!/usr/bin/env python
# coding: utf-8

# # MNIST With PyTorch Training
# This program runs in about 52.337 seconds (Windows 11, i7, 16 GB)

# ## Prerequisites
# Install the following packages



from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.Shell import Shell


# ## Import Libraries



StopWatch.start('total')
StopWatch.start('import')
StopWatch.progress(0)

import os    # noqa: E402
import cpuinfo    # noqa: E402
import torch    # noqa: E402
from torchvision import datasets, transforms    # noqa: E402
from torch import nn    # noqa: E402
from torch import optim    # noqa: E402
from keras.datasets import mnist    # noqa: E402
from cloudmesh.common.systeminfo import os_is_windows    # noqa: E402

StopWatch.stop('import')
StopWatch.progress(6)


# ## Data Load



StopWatch.start("data-load")

(x_train, y_train), (x_test, y_test) = mnist.load_data()

StopWatch.stop("data-load")
StopWatch.progress(7)


# ## Pre-Process Data
# 
# Here we download the data using PyTorch data utils and transform the data by using a normalization function. PyTorch provides a data loader abstraction called a `DataLoader` where we can set the batch size, data shuffle per batch loading. Each data loader expecte a Pytorch Dataset. The DataSet abstraction and DataLoader usage can be found [here](https://pytorch.org/tutorials/recipes/recipes/loading_data_recipe.html) 



StopWatch.start("data-pre-process")

# Data transformation function
transform = transforms.Compose([transforms.ToTensor(),
                              transforms.Normalize((0.5,), (0.5,)),
                              ])

# DataSet
train_data_set = datasets.MNIST('pytorch/My Drive/mnist/data/', download=True, train=True, transform=transform)
validation_data_set = datasets.MNIST('pytorch/My Drive/mnist/data/', download=True, train=False, transform=transform)

train_loader = torch.utils.data.DataLoader(train_data_set, batch_size=32, shuffle=True)
validation_loader = torch.utils.data.DataLoader(validation_data_set, batch_size=32, shuffle=True)

StopWatch.stop("data-pre-process")
StopWatch.progress(8)


# ## Define Model
# 
# Here we select the matching input size compared to the network definition. 
# Here data reshaping or layer reshaping must be done to match input data shape with the network input shape. Also we define a set of hidden unit sizes along with the output layers size. The `output_size` must match with the number of labels associated with the classification problem. The hidden units can be chosesn depending on the problem. `nn.Sequential` is one way to create the network. Here we stack a set of linear layers along with a softmax layer for the classification as the output layer. 



StopWatch.start("define-model")

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

StopWatch.stop("define-model")
StopWatch.progress(9)


# ## Define Loss Function and Optimizer
# 
# Read more about [Loss Functions](https://pytorch.org/docs/stable/nn.html#loss-functions) and [Optimizers](https://pytorch.org/docs/stable/optim.html) supported by PyTorch.
# 
# 
# 
# 



StopWatch.start('define-loss')

criterion = nn.NLLLoss()
optimizer = optim.SGD(model.parameters(), lr=0.003, momentum=0.9)

StopWatch.stop('define-loss')
StopWatch.progress(10)


# # Model Training



StopWatch.start('train')

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

StopWatch.stop('train')
StopWatch.progress(95)


# ## Test
# 
# Similar to training data loader, we use the validation loader to load batch by batch and run the feed-forward network to get the expected prediction and compared to the label associated with the data point. 



StopWatch.start('test')

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

StopWatch.stop('test')
StopWatch.stop('total')
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


# ### Reference: 
# 
# 1. [Torch NN Sequential](https://pytorch.org/docs/stable/generated/torch.nn.Sequential.html)
# 2. [Handwritten Digit Recognition Using PyTorch — Intro To Neural Networks](https://towardsdatascience.com/handwritten-digit-mnist-pytorch-977b5338e627)
# 3. [MNIST Handwritten Digit Recognition in PyTorch](https://nextjournal.com/gkoehler/pytorch-mnist)
# 
