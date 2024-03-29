# -*- coding: utf-8 -*-
"""data_loader.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_VO5SaW-TJ8zC4gIxIWkIWnjV9NLCkxl
"""

from os import listdir
from PIL import Image
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from numpy import asarray

def load_mask_names(path):
    src_list = listdir(path)
    src_list.sort()
    return src_list

def load_image_names(path):
    tar_list = listdir(path)
    tar_list.sort()
    return tar_list

def load_masks(path, src_list_names, size=(256, 256)):
    src_list = list()
    for fn in src_list_names:
        for filename in listdir(path):
            if fn == filename:
                src_img = load_img(path + filename, target_size=size)
                src_img = img_to_array(src_img)
                src_list.append(src_img)
                break
    return asarray(src_list)

def load_images(path, tar_list_names, size=(256, 256)):
    tar_list = list()
    for fn in tar_list_names:
        for filename in listdir(path):
            if fn == filename:
                img = Image.open(path + filename)
                imarray = np.array(img, dtype='float')
                if imarray.shape[0] != size[0] or imarray.shape[1] != size[1]:
                    nimg = img.resize(size)
                    imarray = np.array(nimg, dtype='float')
                tar_list.append(imarray)
                break
    return asarray(tar_list)

def preprocess_data(data):
    X1, X2 = data[0], data[1]
    X1 = (X1 - 127.5) / 127.5
    X2 = (X2 - 127.5) / 127.5
    return [X1, X2]