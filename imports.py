# -*- coding: utf-8 -*-
"""imports.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V_XLybWTA33-YK9A09ljbCs54-CxMolD
"""

# imports.py
import os
import shutil
import numpy as np
import pickle
import glob
import tensorflow as tf
import matplotlib.image as mpimg
from PIL import Image
import matplotlib.pyplot as plt
import math
import cv2
import torch
from tensorflow import keras
from keras.optimizers import Adam, SGD
from keras.callbacks import ModelCheckpoint
from keras.models import Sequential, Model, load_model
from keras.layers import Dense, Input, Dropout, Activation, Flatten, BatchNormalization, ReLU, LeakyReLU, concatenate
from keras.layers import Conv2D, MaxPooling2D, UpSampling2D, AveragePooling2D, GlobalAveragePooling2D, Add
from keras.metrics import MeanIoU
from os.path import join, isdir
from os import listdir, rmdir
from shutil import move, rmtree, make_archive
from tensorflow.keras.losses import categorical_crossentropy
import tensorflow.keras.backend as K