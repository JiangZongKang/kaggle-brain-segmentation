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
        # read images
        volumes = {}
        masks = {}
        print('reading {} images ...'.format(subset))
        for (dirpath, dirnames, filenames) in os.walk(images_dir):
            image_slices = []
            mask_slices = []
            for filename in sorted(filter(lambda f: '.tif' in f, filenames),
                                   key=lambda x: int(x.split('.')[-2].split('_')[4])):
                filepath = os.path.join(dirpath, filename)
                if 'mask' in filename:
                    mask_slices.append(imread(filepath, as_gray=True))
                else:
                    image_slices.append(imread(filepath))
                if len(image_slices) > 0:
                    patient_id = dirpath.split('/')[-1]
                    volumes[patient_id] = np.array(image_slices[1:-1])
                    masks[patient_id] = np.array(mask_slices[1: -1])

                self.patients = sorted(volumes)

                # select cases to subset
                if not subset == 'all':
                    random.seed(seed)
                    validation_patients = random.sample(self.patients, k=validation_cases)
                    if subset == 'validation':
                        self.patients = validation_patients
                    else:
                        self.patients = sorted(list(set(self.patients).difference(validation_patients)))

                print('preprocessing {} volumes...'.format(subset))



