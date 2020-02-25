# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 18:40:10 2020

@author: zqd-d
"""
import os
filePath = 'C:\\Users\\zqd-d\\Desktop\\train\\' #path of the folder which contains all training data in png format.

fpng_names =os.listdir(filePath) #names of the labels 
#print(fpng_names)
print(len(fpng_names))  #get the account of the labels
i=0
with open('C:\\Users\\zqd-d\\Desktop\\groundtruth_train\\all_to_split.tsv','r')as flabel: #open the checking file which contains labels(groundtruth)
    lines = flabel.readlines()
    
    for line in lines:
        
        if line.split()[0]+'.png' in fpng_names: #if the label is overthere, account plus 1
            i+=1
            
        else: #if it isn't there print its name
            print(line)
            #print(line.split()[0]+'.png')
    print(i) #the account of contained groundtruth
