#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
@author: JiangZongKang
@contact: jzksuccess@gmail.com
@software: Pycharm
@file: dataset.py
@time: 2019/8/3 11:10

'''

import os
import random
import numpy as np
import torch
from skimage.io import imread
from torch.utils.data import Dataset
from utils import crop_sample, pad_sample, resize_sample, normalize_volume

class BrainSegmentationDataset(Dataset):
    'Brain MRI dataset for Flair abnormality'

    in_channels = 3
    out_channels = 1

    def __init__(self, image_dir, transform=None, image_size=256, suset='train', random_sampling=True, validation_cases=10, seed=7):
        assert subset in ['all', 'train', 'validation']