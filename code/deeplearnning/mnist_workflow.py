import numpy as np
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
from cloudmesh.cc.workflow import Workflow
from cloudmesh.cc.workflow import Graph
import os.path
from pprint import pprint
import shelve
import pytest
from cloudmesh.cc.queue import Queues
from cloudmesh.common.Benchmark import Benchmark
from cloudmesh.common.util import HEADING
from cloudmesh.common.systeminfo import os_is_windows
from cloudmesh.common.Shell import Shell
import networkx as nx
from cloudmesh.common.variables import Variables
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
import shutil
from cloudmesh.common.util import banner
from cloudmesh.common.StopWatch import StopWatch

g = Graph()

(x_train, y_train), (x_test, y_test) = mnist.load_data()

