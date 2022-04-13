# The goal of this program is to move any image files into a new Images folder.

import os
import shutil
import glob

images = [f for f in os.listdir() if '.jpg' in f.lower()]

path = '/home/nero/Downloads/it_dev/python/images'
isdir = os.path.isdir(path) 

if isdir == False:
    os.mkdir('images')


for jpg in glob.glob(".jpg"):
    new_path = 'images/' + jpg
    shutil.move(jpg,'images')

#for image in images:
#    new_path = 'images/' + image
#    shutil.move(image, new_path)
