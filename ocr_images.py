import os
import subprocess
import sys
import io
import numpy as np
import glob
import cv2
import time
import shutil
from google.cloud import vision
from google.cloud.vision import types

def annotation_fp (fp):
    filename = '{:03}.json'.format(int(
        fp
        .split('/')[-1]
        .split('_')[-1]
        .replace('.jpg', '')
    ))
    return '/'.join(fp.split('/')[:-1]) + '/{}'.format(filename)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'seattlecitysellers-cloud.json'

def detect_document (path):
    '''Detects document features in an image.'''
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)
    return client.document_text_detection(image=image)
    
c = 0
for record_img_fp in glob.glob('boxes/box_*/record_*/*.jpg'):
    dest_fp = annotation_fp(record_img_fp)
    if not os.path.isfile(dest_fp):
        print('-- new query --')
        print('    using {}\n    saving to {}'.format(record_img_fp, dest_fp))
        response = detect_document(record_img_fp)
        with open(dest_fp, 'wb') as dest:
            dest.write(response.SerializeToString())
    else:
        print('skipping {}, exists'.format(dest_fp))
    c += 1
    if (c % 25) == 0:
        print('{} done'.format(c))
#for box_number in range(1, 21):
#    box_path = 'boxes/box_{}'.format(box_number)
#    records = sorted(glob.glob(box_path + '/record_*'), key=int_name)
#    for record in records:
#        img_cnt = 1
#        for record_img in glob.glob(record + '/*.jpg'):
#            shutil.copy(record_img, 'dropbox/{:04}-img-{:03}-box-{:03}.jpg'.format(c, img_cnt, box_number))
#            img_cnt += 1
#        c += 1
#
#print(c)
#
#
## The name of the image file to annotate
#file_name = 'records_cropped/0002-img-001-box-001.jpg'
#detect_document(file_name)
