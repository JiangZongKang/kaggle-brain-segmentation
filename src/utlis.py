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

def dsc(y_pred, p_true, lcc=True):
    if lcc and np.any(y_pred):
        y_pred = np.round(y_pred).astype(int)
        y_true = np.round(y_true).astype(int)
        y_pred = largest_connected_component(y_pred)

    return np.sum(y_pred[y_true == 1]) * 2.0 / (np.sum(y_pred) + np.sum(y_true))
