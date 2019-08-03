#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
@author: JiangZongKang
@contact: jzksuccess@gmail.com
@software: Pycharm
@file: utlis.py
@time: 2019/8/3 12:59

'''
import numpy as np
from medpy.filter.binary import largest_connected_component
from skimage.exposure import rescale_intensity
from skimage.transform import resize

def dsc(y_pred, y_true, lcc=True):
    if lcc and np.any(y_pred):
        y_pred = np.round(y_pred).astype(int)
        y_true = np.round(y_true).astype(int)
        y_pred = largest_connected_component(y_pred)

    return np.sum(y_pred[y_true == 1]) * 2.0 / (np.sum(y_pred) + np.sum(y_true))

def crop_image(x):
    volume, mask = x
    volume[volume < np.max(volume) * 0.1] = 0
    z_projection = np.max(np.max(np.max(volume, axis=-1), axis=-1), axis=-1)
    z_nozero = np.nonzero(z_nozero)
    z_min = np.min(z_nozero)
    z_max = np.max(z_nozero) +1
    y_projection = np.max(np.max(np.max(volume, axis=0), axis=-1), axis=-1)
    y_nozero = np.nonzero(y_nozero)
    y_min = np.min(y_nozero)
    y_max = np.max(y_nozero) + 1
    x_projection = np.max(np.max(np.max(volume, axis=0), axis=0), axis=-1)
    x_nozero = np.nonzero(x_nozero)
    x_min = np.min(x_nozero)
    x_max = np.max(x_nozero) + 1
    return (volume[z_min:z_max, y_min:y_max, x_min:x_max],
            mask[z_min:z_max, y_min:y_max, x_min:x_max])

def pad_image(x):
    volume, mask = x
    a = volume.shape[1]
    b = volume.shape[2]
    if a == b:
        return  volume, mask
    diff = (max(a, b) - min(a, b)) / 2.0
    if a > b:
        padding = ((0, 0), (0, 0), (int(np.floor(diff)), int(np.ceil(diff))))
    else:
        padding = ((0, 0), (int(np.floor(diff)), int(np.ceil(diff))), (0, 0))
    mask = np.pad(mask, padding, mode='constant', constant_values=0)
    padding = padding + ((0, 0),)
    volume = np.pad(volume, padding, mode='constant', constant_values=0)
    return volume, mask


