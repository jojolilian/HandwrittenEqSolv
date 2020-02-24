# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 18:40:10 2020

@author: zqd-d
"""
import os
filePath = 'C:\\Users\\zqd-d\\Desktop\\train\\'

fpng_names =os.listdir(filePath)
#print(fpng_names)
print(len(fpng_names))
i=0
with open('C:\\Users\\zqd-d\\Desktop\\groundtruth_train\\all_to_split.tsv','r')as flabel:
    lines = flabel.readlines()
    
    for line in lines:
        
        if line.split()[0]+'.png' in fpng_names:
            i+=1
            
        else:
            print(line)
            #print(line.split()[0]+'.png')
    print(i)