# -*- coding: utf-8 -*-
"""ssim_calculator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12-GY8FqG0mXVX-fCD2SbsLeViJba55o_
"""

import numpy as np
from scipy import signal

def calculate_ssim(img1, img2):
    K1 = 0.0003
    K2 = 0.0009
    win_size = 11

    img1 = img1.astype(np.float64)
    img2 = img2.astype(np.float64)

    # Compute means
    mu1 = signal.convolve2d(img1.mean(axis=-1), np.ones((win_size, win_size)), mode='valid') / win_size ** 2
    mu2 = signal.convolve2d(img2.mean(axis=-1), np.ones((win_size, win_size)), mode='valid') / win_size ** 2

    # Compute variances and covariances
    sigma1_sq = signal.convolve2d(img1.mean(axis=-1) ** 2, np.ones((win_size, win_size)), mode='valid') / win_size ** 2 - mu1 ** 2
    sigma2_sq = signal.convolve2d(img2.mean(axis=-1) ** 2, np.ones((win_size, win_size)), mode='valid') / win_size ** 2 - mu2 ** 2
    sigma12 = signal.convolve2d(img1.mean(axis=-1) * img2.mean(axis=-1), np.ones((win_size, win_size)), mode='valid') / win_size ** 2 - mu1 * mu2

    # Constants
    C1 = (K1 * 255) ** 2
    C2 = (K2 * 255) ** 2

    # Compute SSIM
    ssim_map = ((2 * mu1 * mu2 + C1) * (2 * sigma12 + C2)) / ((mu1 ** 2 + mu2 ** 2 + C1) * (sigma1_sq + sigma2_sq + C2))

    return np.mean(ssim_map)