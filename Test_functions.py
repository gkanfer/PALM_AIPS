#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:12:23 2021

@author: kanferg
"""
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageEnhance
#from PIL import fromarray
from skimage import data,io
from skimage.filters import threshold_otsu, threshold_local, threshold_local
from skimage.morphology import convex_hull_image
import matplotlib.pyplot as plt
import scipy as ndimage
from scipy.ndimage.morphology import binary_opening
from skimage.morphology import disk
from skimage.segmentation import watershed
from skimage import data
from skimage.filters import rank
from skimage.util import img_as_ubyte
from skimage import data, util
from skimage.measure import label
from skimage.measure import perimeter
from skimage import measure
from skimage import exposure, io, util
import os, re
import pandas as pd
from pandas import DataFrame
from scipy.ndimage import label, generate_binary_structure
from scipy.ndimage.morphology import binary_fill_holes
from scipy.ndimage import generic_filter
import cv2
import glob
from scipy import ndimage, misc

#from util import noise_model

os.chdir('/Users/kanferg/Desktop/Gil_LabWork/ANNA-PALM/Simulator/Similtor_genration/Noise_simulator')
ret,orig_21=cv2.imreadmulti('21.tif', [], cv2.IMREAD_ANYDEPTH)
np.shape(orig_21)
print(orig_21)



###################
# Calculate offset
##################
#1) Photon per pixel = (electrons (grey-value / conversion coefficent 0.49 for the flash 4)/0.83 (QE)))   
#2) Oi = summary of photon per pixel accrose frame / Total number of frame 

# First turn all to large data frame using panda

e_ctrl, Offset_ctrl= sCEMOS_offset(image=orig_21,M=3000,h=64,l=64,CC=0.49,QE=0.83,Print_i = True, Image_mode=256)

#####################
# Calculate Variance
#####################
# calculate for 60,000 frame (in this example I have only 3000)
#electron**2 - offset**2

Var_df_sum = sCEMOS_Variance(elec=e_ctrl, Offset_df=Offset_ctrl, M=3000, h=64, l=64)
    
#####################
# Calculate Gain
#####################
#K total number illumination (21 to 200 photon per pixel) we have 5 illumination
#vi in k variance of illumination k minus the previus veriation at K
#Di in K is the mean of the electron count in sequance k minus oi that was calculated previsuly

# first Calculate matrix A
#Upload list name
Path_glob_noise="/Users/kanferg/Desktop/Gil_LabWork/ANNA-PALM/Simulator/Similtor_genration/Circle/img/"
os.chdir(Path_glob_noise)
files = glob.glob(os.path.join(Path_glob_noise, '*.tif'))
files.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])

#import pdb



k=5
Ai = np.empty((0,64,64),float)
Bi = np.empty((0,64,64),float)
for i in range(k):
    reg, img_temp=cv2.imreadmulti(files[i], [], cv2.IMREAD_ANYDEPTH)
    electron_temp, Offset_temp = sCEMOS_offset(image=img_temp,M=3000,h=64,l=64,CC=0.49,QE=0.83,Print_i = True, Image_mode=256)
    Var_df_sum_temp = sCEMOS_Variance(elec=electron_temp, Offset_df=Offset_temp, M=3000, h=64, l=64)
    Ai_temp=Var_df_sum_temp-Var_df_sum
    #pdb.set_trace()
    Dk = electron_temp.mean(axis=0,keepdims=True)
    Bi_temp = Dk - Offset_temp
    Ai=np.concatenate([Ai, Ai_temp],axis=0)
    Bi=np.concatenate([Bi, Bi_temp],axis=0)

# BiT=np.array([Bi[0].T,Bi[1].T])
# AiT=np.array([Ai[0].T,Ai[1].T])
# gi=(1/(Bi*(BiT))*(Bi*(AiT)))

i=1
gi = np.empty((0,64,64),float)
for i in range(np.shape(Ai)[0]):
    #BiT_temp=np.array([Bi[0].T,Bi[0].T])
    #AiT_temp=np.array([Ai[0].T,Ai[0].T])
    BiT_temp=np.array(Bi[i].T)
    AiT_temp=np.array(Ai[i].T)
    firstArg=Bi[i]*(BiT_temp)
    firstArg=firstArg+0.00000000001
    gi_temp=(1/firstArg)*(Bi[i]*(AiT_temp))
    gi_temp=gi_temp.reshape(1,64,64)
    gi=np.concatenate([gi, gi_temp],axis=0)

plt.hist(BiT, bins='auto')  # arguments are passed to np.histogram
plt.show()



# translate from Matlab SMSN_single_sCMOS function

#####################
# SEGMENTATION
#####################
psfsigma=1.29 #in pixel
iternation=50
fittype=1  # 1 - fit: x,y,photon,bg 2- fit: PSF, sigma
llr_threshold=100 #log likelihood ratio thrsheold 
zm=50 
boxsz=7 #pixel 

# suboffsetmap=Offset_ctrl
# subvarmap=Var_df_sum
# subgainmap=gi
# ims=files[0]

offsetim= Offset_ctrl       #repmat(offset,[1 1 size(ims,3)]);
varim= Var_df_sum          #repmat(var,[1 1 size(ims,3)]);
gainim= gi         #repmat(gain,[1 1 size(ims,3)]);
fin= (files[0]- offsetim)/gainim           #(single(ims)-single(offsetim))./single(gainim);

# from matlab:
# [subregion t l subvarim subgainim]=image_segmentation_sCMOS(fin,varim,gainim,boxsz);















