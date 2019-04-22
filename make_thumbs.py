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
import cv2

def int_name (fp):
    return int(
        fp
        .split('/')[-1]
        .split('_')[-1]
    )

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

resize_x = 512

for box_number in range(1, 21):
    box_path = 'thumbs/box_{}'.format(box_number)
    records = sorted(glob.glob(box_path + '/record_*'), key=int_name)
    for record in records:
        for record_img in glob.glob(record + '/*.jpg'):
            thumb = image_resize(cv2.imread(record_img), width=300)
            cv2.imwrite(record_img, thumb)
            print(record_img)
