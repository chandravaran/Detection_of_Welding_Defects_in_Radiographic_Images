# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 08:26:13 2020

@author: Chandravaran K V
"""
#This program finds images which have same size and stores the size of them into Excel later on 

import numpy as np
import os
import cv2
import collections

images_D = 'F:\\IP_mini_project\\RT Training Images DGI'
dic = collections.defaultdict(int)
c=0
l=[]
for f in os.listdir(images_D):
    i = cv2.imread(os.path.join(images_D, f))
    d = i.shape                                     #finding shape
    dic[d] += 1                                     #adding it into dictonary or incrementing value if it exits
    l.append([d,f])
    c+=1
    print(c)
print(dic)

ans=0
for c in dic.values():
    ans+=c
print(ans)

c=0
for f in os.listdir(images_D):
    c+=1
print(c)  

        
with open('image_size_file.csv', 'w') as f:
    for i in l:
        f.write("%s\n"%(i))
  
  
