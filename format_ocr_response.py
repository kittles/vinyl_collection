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
from google.cloud.vision_v1.proto import image_annotator_pb2
import json
from google.protobuf.json_format import MessageToJson

parsed = image_annotator_pb2.AnnotateImageResponse()

## fix the naming issue...
#for annotation_fp in glob.glob('boxes/box_*/record_*/*.json'):
#    raw_fp = annotation_fp.replace('.json', '.raw')
#    with open(raw_fp, 'rb') as f:
#        data = parsed.FromString(f.read())
#        json_data = json.loads(MessageToJson(data))
#        with open(annotation_fp, 'w') as dest:
#            dest.write(json.dumps(json_data, indent=4))

#c = 0
#for annotation_fp in glob.glob('boxes/box_*/record_*/*.json'):
#    c += 1
#    json_data = json.loads(open(annotation_fp, 'r').read())
#    try:
#        text = ' '.join([i['description'] for i in json_data['textAnnotations']])
#    except:
#        text = ''
#    dest_fp = annotation_fp.replace('.json', '.txt')
#    if os.path.isfile(dest_fp):
#        continue
#    with open(dest_fp, 'w') as dest:
#        dest.write(text)
#    if c % 25 == 0:
#        print(c)


#html_fp = 'table_data.html'
#dest = open(html_fp, 'w')
#c = 0
#for record_fp in glob.glob('boxes/box_*/record_*'):
#    front_img_url = record_fp.replace('boxes', 'thumbs') + '/001.jpg'
#    back_img_url = record_fp.replace('boxes', 'thumbs') + '/002.jpg'
#    text = open(record_fp + '/001.txt', 'r').read() + ' ' + open(record_fp + '/002.txt', 'r').read()
#    new_row = '<tr> <td><img src="{}"/></td> <td><img src="{}"/></td> <td>{}</td> </tr>\n'.format(front_img_url, back_img_url, text)
#    dest.write(new_row)
#    if c % 25 == 0:
#        print(c)
#dest.close()

# make sql table
#import psycopg2
#
#connect_str = "dbname='vinyl' user='patrick' host='localhost' password=''"
#conn = psycopg2.connect(connect_str)
#cur = conn.cursor()
#cur.execute("""CREATE TABLE records (
#	id SERIAL PRIMARY KEY,
#	front TEXT,
#	back TEXT,
#	jacket_text TEXT
#);""")
#c = 0
#for record_dir in glob.glob('boxes/box_*/record_*/'):
#	c += 1
#	jacket_text = open(record_dir + '/001.txt', 'r').read()
#	jacket_text += ' '
#	jacket_text += open(record_dir + '/002.txt', 'r').read()
#	front = record_dir + '/001.jpg'
#	back = record_dir + '/002.jpg'
#
#	sql = '''
#		INSERT INTO records
#			(front, back, jacket_text) 
#		VALUES 
#			(%s, %s, %s);
#	'''
#	cur.execute(sql, (front, back, jacket_text))
#conn.commit() # <--- makes sure the change is shown in the database
#conn.close()
#cur.close()
