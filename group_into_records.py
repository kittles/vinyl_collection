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

template = cv2.imread('template_big.jpg',0)
w, h = template.shape[::-1]
cv2.namedWindow('detected', cv2.WINDOW_NORMAL)

def int_name (fp):
    return int(
        fp
        .split('/')[-1]
        .split('-')[-1]
        .replace('.jpg', '')
    )

for box_number in range(8, 21):
    if box_number == 19:
        continue
    if box_number == 1:
        continue
    box_path = 'boxes/box_{}'.format(box_number)
    box = sorted(glob.glob(box_path + '/*.jpg'), key=int_name)
    groups = []
    current_group = []
    for img_fp in box:
        print(img_fp)
        img = cv2.imread(img_fp, 0)
        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where( res >= 0.8) 
        if len(loc[0]):
            if len(current_group):
                groups.append(current_group[:])
            current_group = []
        else:
            current_group.append(img_fp)

        #for pt in zip(*loc[::-1]): 
        #    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2) 
          
        # Show the final image with the matched area. 

    final_groups = []
    for idx, group in enumerate(groups):
        # picture of front and back assumed, normal
        if len(group) == 2:
            final_groups.append(group)
            continue
        # more than two images, need to disambiguate
        else:
            print('some extra images')

        # need to split the group into smaller groups

        imgs = []
        imgs_fps = []
        for img_fp in group:
            img = cv2.imread(img_fp)
            imgs.append(cv2.resize(img, (640, 480)))
            imgs_fps.append(img_fp)

        while imgs:
            all_img = np.concatenate(imgs, axis=1)
            cv2.imshow('detected', all_img) 
            take_n = int(cv2.waitKey(0)) - 48
            # 49 is number 1
            print('taking first ', take_n)
            [imgs.pop(0) for _ in range(take_n)]
            final_groups.append([imgs_fps.pop(0) for _ in range(take_n)])

    for idx, group in enumerate(final_groups):
        record_dir = box_path + '/record_{:04}'.format(idx + 1)
        try:
            os.mkdir(record_dir)
        except:
            pass

        for img_idx, img_fp in enumerate(group):
            dest = record_dir + '/{:03}.jpg'.format(img_idx + 1)
            shutil.copyfile(img_fp, dest)

cv2.destroyAllWindows()
