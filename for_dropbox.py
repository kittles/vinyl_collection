import numpy as np
import glob
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn import datasets, svm, metrics
import time
import os
import shutil

def int_name (fp):
    return int(
        fp
        .split('/')[-1]
        .split('_')[-1]
    )

dropbox_fp = 'dropbox/'
c = 1
for box_number in range(1, 21):
    box_path = 'boxes/box_{}'.format(box_number)
    records = sorted(glob.glob(box_path + '/record_*'), key=int_name)
    for record in records:
        img_cnt = 1
        for record_img in glob.glob(record + '/*.jpg'):
            shutil.copy(record_img, 'dropbox/{:04}-img-{:03}-box-{:03}.jpg'.format(c, img_cnt, box_number))
            img_cnt += 1
        c += 1

print(c)
