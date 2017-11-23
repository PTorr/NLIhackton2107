'''
This script makes a hdf5 style dataset with all images in a chosen directory.
Gram matrices computed here are never normalized by the number of channels.
Normalization is done if necessary on the training stage.
'''
import pickle
import numpy as np
import h5py

import keras
import keras.backend as K
from keras.applications import vgg16

from training import get_style_features
from utils import preprocess_image_scale, config_gpu, std_input_list

import os
import argparse
from PIL import Image
from PIL import Image

# def_sl = ['block1_conv2', 'block2_conv2','block3_conv3', 'block4_conv3']
def_sl = ['block1_conv2'] # Use this for just the first conv layer
# def_sl = ['block4_conv3'] # Use this for just the last conv layer

style_dir = 'maps'
gpu = None
style_imgs = None
style_img_size= [None]
style_layers=def_sl
gpu=''
allow_growth=False
config_gpu(gpu, allow_growth)

loss_net = vgg16.VGG16(weights='imagenet', include_top=False)

targets_dict = dict([(layer.name, layer.output) for layer in loss_net.layers])

s_targets = get_style_features(targets_dict, style_layers)

get_style_target = K.function([loss_net.input], s_targets)
gm_lists = [[] for l in style_layers]

img_list = []
img_size_list = []
# Get style image names or get all images in the directory
if style_imgs is None:
    style_imgs = os.listdir(style_dir)

# Check the image sizes
style_img_size = std_input_list(style_img_size, len(style_imgs), 'Image size')

for img_name, img_size in zip(style_imgs, style_img_size):
    try:
        print(img_name)
        img = preprocess_image_scale(os.path.join(style_dir, img_name),
                                     img_size=img_size)
        s_targets = get_style_target([img])
        for l, t in zip(gm_lists, s_targets):
            l.append(t)
        img_list.append(os.path.splitext(img_name)[0])
        img_size_list.append(img_size)
    except IOError as e:
        print('Could not open file %s as image.' %img_name)

mtx = []
for l in gm_lists:
    mtx.append(np.concatenate(l))
mtx = mtx[0]
pickle.dump(mtx, open('{}.pickle'.format(style_dir),'wb'),protocol=2)




style_dir = 'maps'
gpu = None
style_imgs = None
style_img_size= [None]
style_layers=def_sl
gpu=''
allow_growth=False
config_gpu(gpu, allow_growth)

loss_net = vgg16.VGG16(weights='imagenet', include_top=False)

targets_dict = dict([(layer.name, layer.output) for layer in loss_net.layers])

s_targets = get_style_features(targets_dict, style_layers)

get_style_target = K.function([loss_net.input], s_targets)
gm_lists = [[] for l in style_layers]

img_list = []
img_size_list = []
# Get style image names or get all images in the directory
if style_imgs is None:
    style_imgs = os.listdir(style_dir)

for img_name in style_imgs[1:]:
    img = Image.open(img_name).convert('LA')
    img.save('{}_greyscale.jpg'.format(img_name))
    

# Check the image sizes
style_img_size = std_input_list(style_img_size, len(style_imgs), 'Image size')

for img_name, img_size in zip(style_imgs, style_img_size):
    try:
        print(img_name)
        img = preprocess_image_scale(os.path.join(style_dir, img_name),
                                     img_size=img_size)
        s_targets = get_style_target([img])
        for l, t in zip(gm_lists, s_targets):
            l.append(t)
        img_list.append(os.path.splitext(img_name)[0])
        img_size_list.append(img_size)
    except IOError as e:
        print('Could not open file %s as image.' %img_name)

mtx = []
for l in gm_lists:
    mtx.append(np.concatenate(l))
mtx = mtx[0]
pickle.dump(mtx, open('{}_greyscale.pickle'.format(style_dir),'wb'),protocol=2)
